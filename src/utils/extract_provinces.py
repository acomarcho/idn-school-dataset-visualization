import pandas as pd

class ExtractProvinces:
  def __init__(self):
    self.unique_provinces = None

  def read(self, filepath):
    dataframe = pd.read_csv(filepath)
    self.unique_provinces = dataframe['province_name'].unique()

  def save_to_file(self, filepath):
    if self.unique_provinces is not None:
      with open(filepath, 'w') as f:
        f.write("\n".join(self.unique_provinces))

if __name__ == '__main__':
  extract_provinces = ExtractProvinces()
  extract_provinces.read('./data/raw_school_data.csv')
  extract_provinces.save_to_file('./out/unique_provinces.txt')