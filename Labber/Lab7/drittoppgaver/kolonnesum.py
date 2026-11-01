import csv
import math


def sum_of_column(path, col):
    total = 0
    with open(path, newline='', encoding='utf-8', errors='replace') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            if col >= len(row):
                continue  
            try:
                value = float(row[col])
            except ValueError:
                continue 
            if math.isfinite(value): 
                total += value
    return total


def test_sum_of_column():
    print('Tester sum_of_column... ', end='')
    assert(42.0 == sum_of_column('foo.csv', 0))
    assert(95.0 == sum_of_column('foo.csv', 1))
    assert(0.0 == sum_of_column('foo.csv', 2))
    assert(76363.0 == sum_of_column('Statistikk_Tilsyn_ar.csv', 1))
    assert(46007.0 == sum_of_column('Statistikk_Tilsyn_ar.csv', 2))
    assert(5024518.0 == sum_of_column('airport-codes.csv', 3))
    print('OK')


if __name__ == '__main__':
    test_sum_of_column()