import pandas as pd
import csv

class BuildCompleteData:
  def __init__(self):
    self.province_mapping_df = pd.read_csv("./data/province_mapping.csv")
    self.province_area_df = pd.read_csv("./data/province_area.csv")
    self.province_population_df = pd.read_csv("./out/extracted_province_data.csv")
    self.province_population_by_age_df = pd.read_csv("./out/extracted_province_data_by_age.csv")
    self.school_data_df = pd.read_csv("./data/raw_school_data.csv")

    self.complete_data_rows = []

  def run(self):
    for index, row in self.school_data_df.iterrows():
      if index % 1000 == 0:
        print(f"Processing index {index}...")

      complete_row = {}
      
      mapped_province_name = self.__map_province_name(row['province_name'])

      complete_row['province_name'] = mapped_province_name
      complete_row['city_name'] = row['city_name']
      complete_row['district_name'] = row['district']
      complete_row['school_name'] = row['school_name']
      complete_row['stage'] = row['stage']
      complete_row['status'] = row['status']
      complete_row['lat'] = row['lat']
      complete_row['long'] = row['long']
      complete_row['province_area'] = self.__get_province_area(mapped_province_name)
      complete_row['total_population'] = self.__get_province_total_population(mapped_province_name)
      complete_row['total_education_age_population'] = self.__get_province_education_age_population(mapped_province_name)

      self.complete_data_rows.append(complete_row)

  def __map_province_name(self, province_name):
    try:
      return self.province_mapping_df[self.province_mapping_df["school_data_name"] == province_name]["bps_name"].values[0]
    except:
      print(f"_map_province_name: Error occured while mapping province_name {province_name}")
      return ""
  
  def __get_province_area(self, province_name):
    try:
      return self.province_area_df[self.province_area_df["province_name"] == province_name]["area_in_km2"].values[0]
    except:
      print(f"__get_province_area: Error occured while mapping province_name {province_name}")
      return 0
    
  def __get_province_total_population(self, province_name):
    try:
      return self.province_population_df[self.province_population_df["province_name"] == province_name]["total_population"].values[0]
    except:
      print(f"__get_province_total_population: Error occured while mapping province_name {province_name}")
      return 0
  
  def __get_province_education_age_population(self, province_name):
    try:
      return self.province_population_by_age_df[self.province_population_by_age_df["province_name"] == province_name]["education_age_population"].values[0]
    except:
      print(f"__get_province_education_age_population: Error occured while mapping province_name {province_name}")
      return 0

  def save_to_csv(self, filepath):
    print("Beginning to save CSV file ...")

    if len(self.complete_data_rows) > 0:
      with open(filepath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(['province_name', 'city_name', 'district_name', 'school_name', 'stage', 'status', 'lat', 'long', 'province_area', 'total_population', 'total_education_age_population'])

        for row in self.complete_data_rows:
          try:
            writer.writerow([row['province_name'], row['city_name'], row['district_name'], row['school_name'], row['stage'], row['status'], row['lat'], row['long'], row['province_area'], row['total_population'], row['total_education_age_population']])
          except:
            print(f"An error occured while writing row {row}")

if __name__ == "__main__":
  build_complete_data = BuildCompleteData()
  build_complete_data.run()
  build_complete_data.save_to_csv('./out/complete_data.csv')