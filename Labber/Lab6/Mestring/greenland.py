import csv
import os
directory_of_current_file = os.path.dirname(__file__)
os.chdir(directory_of_current_file)


def total_volume(path):
    volume = 0

    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            area = float(row["area_km2"])
            thickness = float(row["mean_thickness_m"])
            volume += area * thickness / 1000

    return volume


def sea_level_rise(path):
    volume = total_volume(path)
    rise = volume / 395000
    return round(rise, 1)


def test_total_volume():
    print('Tester total_volume... ', end='')
    assert round(total_volume('greenland.csv')) == 2829200
    print('OK')


def test_sea_level_rise():
    print('Tester sea_level_rise... ', end='')
    assert sea_level_rise('greenland.csv') == 7.2
    print('OK')


if __name__ == '__main__':
    test_total_volume()
    test_sea_level_rise()
    print(total_volume('antarctica.csv'))
    print(sea_level_rise('antarctica.csv'))