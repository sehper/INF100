import csv
import os


def combine_csv_in_dir(dirpath, result_path):
    header = ["uibid", "karakter", "kommentar"]
    rows = []

    for filename in os.listdir(dirpath):
        if not filename.endswith(".csv"):
            continue
        filepath = os.path.join(dirpath, filename)
        with open(filepath, "rt", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  
            for row in reader:
                if row:  
                    rows.append(row)

    with open(result_path, "wt", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)