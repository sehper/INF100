from pathlib import Path
import json

def load_emission_data(filename):
    file_path = Path(filename)
    data = json.loads(file_path.read_text())
    return data

def get_deviations(data):
    deviations = []

    for point in data["data"]:
        forecast = point["intensity"]["forecast"]
        actual = point["intensity"]["actual"]

        if forecast is not None and actual is not None:
            deviations.append(abs(forecast - actual))

    return deviations

def count_values_larger_than(values, threshold):
    count = 0

    for value in values:
        if value > threshold:
            count += 1

    return count

def main():
    filename = input()
    threshold = int(input())

    data = load_emission_data(filename)
    deviations = get_deviations(data)
    count = count_values_larger_than(deviations, threshold)

    print(f"Antall avvik større enn {threshold}: {count}")

if __name__ == "__main__":
    main()