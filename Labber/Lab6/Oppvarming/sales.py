import csv

def total_income(path):
    total = 0

    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += (int(row["price"]) - int(row["production_cost"])) * int(row["sold"])

    return total


def test_total_income():
    print('Tester total_income... ', end='')
    expected = (
        (50 - 10) * 100
        + (100 - 20) * 50
        + (500 - 50) * 10
        + (1000 - 100) * 5
        + (10000 - 500) * 2
    )
    actual = total_income('sales.csv')
    assert expected == actual, f'{expected=}, {actual=}'
    print('OK')

test_total_income()