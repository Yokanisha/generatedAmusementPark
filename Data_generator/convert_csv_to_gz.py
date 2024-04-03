import gzip
import csv
import os

def csv_to_gzip(input_csv_file, output_gzip_file):
    if not os.path.exists(input_csv_file):
        print("The input file does not exist.")
        return

    with open(input_csv_file, 'r', newline='') as csvfile:
        with gzip.open(output_gzip_file, 'wt', compresslevel=9) as gzfile:
            reader = csv.reader(csvfile)
            writer = csv.writer(gzfile)
            for row in reader:
                writer.writerow(row)

    print("Conversion completed.")

input_csv_file = 'example.csv' 
output_gzip_file = 'example.csv.gz'

csv_to_gzip(input_csv_file, output_gzip_file)
