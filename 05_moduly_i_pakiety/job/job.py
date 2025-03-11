from extractors.extract import extract
from loaders.load import load
from transformations.transform import transform

def job(input_path, output_path):
  source_data = extract(input_path)
  transformed_data = transform(source_data)
  load(transformed_data, output_path)
