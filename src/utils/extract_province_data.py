import json
import csv

class ExtractProvinceData:
  def __init__(self):
    self.filtered_data = None

  def read(self, filepath):
    with open(filepath, 'r') as file:
      json_data = json.load(file)
      
    filtered_items = [
      item for item in json_data["data"]
      if item["nama_item__kategori_1"] == "Total" and item["nama_item__kategori_2"] == "Total"
    ]

    self.__process_filtered_items(filtered_items)

  def __process_filtered_items(self, filtered_items):
    self.filtered_data = []
    for item in filtered_items:
      self.filtered_data.append({
        'province_name': item['nama_wilayah'],
        'total_population': item['nilai']
      })

  def save_to_csv(self, filepath):
    if self.filtered_data is not None:
      with open(filepath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(['province_name', 'total_population'])

        for datum in self.filtered_data:
          writer.writerow([datum['province_name'], datum['total_population']])

if __name__ == '__main__':
  extract_province_data = ExtractProvinceData()
  extract_province_data.read("./data/raw_province_data.json")
  extract_province_data.save_to_csv("./data/extracted_province_data.csv")