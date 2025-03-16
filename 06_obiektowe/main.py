import argparse
from job import Job

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Job")
    parser.add_argument('--input_path', type=str, help="CSV input")
    parser.add_argument('--output_path', type=str, help="JSON output")
    args = parser.parse_args()

    job = Job(args.input_path, args.output_path)
    job.run()