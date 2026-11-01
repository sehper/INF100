import os
directory_of_current_file = os.path.dirname(__file__)
os.chdir(directory_of_current_file)

def good_style(source_code):
    lines = source_code.splitlines(keepends=True)

    for line in lines:
        if line.endswith('\n'):
            if len(line) > 80:
                return False
        else:
            if len(line) >= 80:
                return False

    return True


def good_style_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        source_code = file.read()

    return good_style(source_code)


def test_good_style():
    print('Tester good_style... ', end='')
    assert good_style('''\
def distance(x0, y0, x1, y1):
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5
''') is True
    assert good_style((('x' * 79) + '\n') * 20) is True
    assert good_style('x' * 80) is False
    assert good_style(
          (('x' * 79) + '\n') * 5
        + (('x' * 80) + '\n')
        + (('x' * 79) + '\n') * 5
    ) is False
    print('OK')


def test_good_style_from_file():
    print('Tester good_style_from_file... ', end='')
    assert good_style_from_file('test_file1.py') is True
    assert good_style_from_file('test_file2.py') is False
    assert good_style_from_file('test_file3.py') is False
    assert good_style_from_file('nice_style.py') is True
    print('OK')


if __name__ == '__main__':
    test_good_style()
    test_good_style_from_file()
