import json
import csv

class ExtractProvinceDataByAge:
  def __init__(self):
    self.filtered_data = None

  def run(self, start_id=1, end_id=35):
    self.filtered_data = []

    for province_id in range(start_id, end_id + 1):
      self.__read(self.__create_path_for_id(province_id))

  def __create_path_for_id(self, id):
    return f"./data/raw_province_data_by_age_{id}.json"

  def __read(self, filepath):
    with open(filepath, 'r') as file:
      json_data = json.load(file)
    
    population_data = {}
    province_name = json_data["data"][0]["nama_wilayah"]

    for entry in json_data["data"]:
      if entry["nama_item__kategori_2"] == "Total":
        population_data[entry['nama_item__kategori_1']] = entry['nilai']

    self.filtered_data.append({
      "province_name": province_name,
      "education_age_population": population_data["0-4"] + population_data["5-9"] + population_data["10-14"] + population_data["15-19"]
    })
    
  def save_to_csv(self, filepath):
    if self.filtered_data is not None:
      with open(filepath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(['province_name', 'education_age_population'])

        for datum in self.filtered_data:
          writer.writerow([datum['province_name'], datum['education_age_population']])

if __name__ == '__main__':
  extract_province_data_by_age = ExtractProvinceDataByAge()
  extract_province_data_by_age.run()
  extract_province_data_by_age.save_to_csv("./out/extracted_province_data_by_age.csv")