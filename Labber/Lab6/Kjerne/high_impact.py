import csv
import os
directory_of_current_file = os.path.dirname(__file__)
os.chdir(directory_of_current_file)

def get_impact(line):
    parts = line.split(';')

    try:
        return float(parts[2])
    except (ValueError, IndexError):
        return None


def filter_earthquakes(earthquake_csv_string, threshold):
    lines = earthquake_csv_string.splitlines()
    result = [lines[0]]

    for line in lines[1:]:
        impact = get_impact(line)

        if impact is not None and impact >= threshold:
            result.append(line)

    return '\n'.join(result) + '\n'


def filter_earthquakes_file(source_filename, target_filename, threshold):
    with open(source_filename, 'r', encoding='utf-8', newline='') as source:
        reader = csv.DictReader(source, delimiter=';')
        rows = [
            row for row in reader
            if get_impact(';'.join([
                row['id'], row['location'], row['impact'], row['time']
            ])) is not None
            and float(row['impact']) >= threshold
        ]

    with open(source_filename, 'r', encoding='utf-8', newline='') as source:
        header = source.readline()

    with open(target_filename, 'w', encoding='utf-8', newline='') as target:
        target.write(header)
        writer = csv.writer(target, delimiter=';', lineterminator='\n')

        for row in rows:
            writer.writerow([
                row['id'], row['location'], row['impact'], row['time']
            ])

def test_get_impact():
    print('Tester get_impact... ', end='')
    assert 1.43 == get_impact('nc72666881;California;1.43;2016-07-27 00:19:43')
    assert 4.9 == get_impact('us20006i0y;Burma;4.9;2016-07-27 00:20:28')
    assert None is get_impact('us20006i0y;Burma;not_a_num;2016-07-27 00:20:28')
    print('OK')

def test_filter_earthquakes():
    print('Tester filter_earthquakes... ', end='')
    input_arg = '''\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
nc72666891;California;0.06;2016-07-27 00:31:37
nc72666892;California;not_a_number;2016-08-23 03:21:18
'''
    # Test 1
    expected_value = '''\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
'''
    actual_value = filter_earthquakes(input_arg, 1.1)
    assert expected_value.strip() == actual_value.strip()

    # Test 2
    expected_value = '''\
id;location;impact;time
us20006i0y;Burma;4.9;2016-07-27 00:20:28
''' 
    actual_value = filter_earthquakes(input_arg, 3.0)
    assert expected_value.strip() == actual_value.strip()

    # Test 3
    expected_value = 'id;location;impact;time\n'
    actual_value = filter_earthquakes(input_arg, 5.0)
    assert expected_value.strip() == actual_value.strip()
    print('OK')


def test_filter_earthquakes_file():
    print('Tester filter_earthquakes_file... ', end='')

    def read_file(path):
        with open(path, 'rt', encoding='utf-8') as f:
            return f.read()

    filter_earthquakes_file('earthquakes_simple.csv',
                            'earthquakes_above_7.csv', 7.0)
    expected_value = (
        'id;location;impact;time\n'
        'us100068jg;Northern Mariana Islands;7.7;2016-07-29 17:18:26\n'
        'us10006d5h;New Caledonia;7.2;2016-08-11 21:26:35\n'
        'us10006exl;South Georgia Island region;7.4;2016-08-19 03:32:22\n'
    )
    actual_value = read_file('earthquakes_above_7.csv')
    assert expected_value.strip() == actual_value.strip()
    print('OK')

if __name__ == '__main__':
    test_get_impact()
    test_filter_earthquakes()
    test_filter_earthquakes_file()