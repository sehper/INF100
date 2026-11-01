from pathlib import Path
import os
directory_of_current_file = os.path.dirname(__file__)
os.chdir(directory_of_current_file)


def main():
    infile = 'sample_in.csv'
    outfile = 'sample_out.csv'
    sep = ';'

    split_dates(infile, outfile, sep)


def split_dates(infile, outfile, sep):
    table = csv_to_table(infile, sep)
    headers = table[0]
    data = table[1:]
    date_col = headers.index('date')

    new_headers = headers + ['year', 'month', 'day']
    new_table = [new_headers]
    for i, row in enumerate(data):
        date = row[date_col].split('.')
        try:
            day = date[0]
            month = date[1]
            year = date[2]
        except IndexError:
            print(f'WARNING! Failed to get date on line {i+2}: {row}')
            day = month = year = ''
        new_row = row + [year, month, day]
        new_table.append(new_row)

    for row in new_table:
        row.pop(date_col)

    table_to_csv(new_table, outfile, sep)
    

def csv_to_table(infile, sep):
    raw_contents = Path(infile).read_text(encoding='utf-8')
    lines = raw_contents.splitlines()
    table = []
    for line in lines:
        row = line.split(sep)
        table.append(row)
    return table


def table_to_csv(table, outfile, sep):
    lines = []
    for row in table:
        line = sep.join(row)
        lines.append(line)
    raw_content = '\n'.join(lines)
    Path(outfile).write_text(raw_content, encoding='utf-8')


if __name__ == '__main__':
    main()