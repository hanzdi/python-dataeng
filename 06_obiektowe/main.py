import argparse
from job import Job
from extractors.extract import CsvExtractor
from transformations.transform import Deduplicator
from loaders.load import JsonLoader

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Job")
    parser.add_argument('--input_path', type=str, help="CSV input")
    parser.add_argument('--output_path', type=str, help="JSON output")
    args = parser.parse_args()

    # Create the ETL components
    extractor = CsvExtractor()
    transformer = Deduplicator(fields=["Imię"])
    loader = JsonLoader(orient="records", index=False, lines=True)

    # Pass them into the job
    job = Job(args.input_path, args.output_path, extractor, transformer, loader)
    job.run()