import os 
directory_of_current_file = os.path.dirname(__file__)
os.chdir(directory_of_current_file)


def get_stringsum(s):
    total = 0

    for word in s.split():
        try:
            total += int(word)
        except ValueError:
            pass

    return total

# def test_get_stringsum():
#     print('Testing get_stringsum... ', end='')
#     assert 6 == get_stringsum('4 2')
#     assert 9 == get_stringsum('5 -1 3 +2')
#     assert 11 == get_stringsum('5 - 1 3 + 2')
#     assert 42 == get_stringsum('42')
#     assert 42 == get_stringsum('forty-one 42 førtitre')
#     assert 42 == get_stringsum('foo2 42 2qux 3x1')
#     assert 0 == get_stringsum('')
#     assert 0 == get_stringsum('foo bar qux')
#     assert 0 == get_stringsum('-9- 3+2')
#     print('OK')

# test_get_stringsum()

#Jeg vet dette ikke blir så fint, men det holder ting ryddig for meg!

def get_line_with_highest_stringsum(s):
    lines = s.splitlines()
    highest_sum = None
    highest_line = 0
    highest_text = ''

    for i, line in enumerate(lines, start=1):
        total = get_stringsum(line)

        if highest_sum is None or total > highest_sum:
            highest_sum = total
            highest_line = i
            highest_text = line

    return highest_line, highest_sum, highest_text

# def test_get_line_with_highest_stringsum():
#     print('Testing get_line_with_highest_stringsum... ', end='')

#     arg = '4 2\n3 3\n6 6 6 6 12 6\n'
#     assert (3, 42, '6 6 6 6 12 6') == get_line_with_highest_stringsum(arg)

#     arg = '4 99 -98\nfoo 42 qux\nfoo bar quz\n'
#     assert (2, 42, 'foo 42 qux') == get_line_with_highest_stringsum(arg)

#     arg = '4 2\n3 3\n'
#     assert (1, 6, '4 2') == get_line_with_highest_stringsum(arg)

#     print('OK')

# test_get_line_with_highest_stringsum()

def main():
    filename = input('Filnavn: ')

    try:
        with open(filename, encoding='utf-8') as file:
            content = file.read()

        i, total, line = get_line_with_highest_stringsum(content)
        print(f'Høyeste strengsum er {total}, funnet først på linje {i}: «{line}»')

    except OSError:
        print('Kunne ikke åpne filen.')


if __name__ == '__main__':
    main()


