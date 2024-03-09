import requests
import json

class DownloadProvinceDataByAge:
  def __init__(self):
    pass

  def run(self, start_id=1, end_id=35):
    base_url = "https://sensus.bps.go.id/topik/tabular/sp2022/188/"

    for id in range(start_id, end_id + 1):
      url = f"{base_url}{id}/3"

      try:
        response = requests.get(url)
        response.raise_for_status()
      except requests.exceptions.RequestException as e:
        print(f"Error downloading data for ID {id}: {e}")
        continue

      data = json.loads(response.text)

      filename = f"./data/raw_province_data_by_age_{id}.json"
      with open(filename, "w") as outfile:
        json.dump(data, outfile, indent=4)

      print(f"Downloaded data for ID {id} and saved to {filename}")

if __name__ == "__main__":
  download_raw_province_data_by_age = DownloadProvinceDataByAge()
  download_raw_province_data_by_age.run(start_id=4, end_id=6)