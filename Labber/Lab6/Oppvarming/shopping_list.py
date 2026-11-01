def shopping_list_to_dict(shopping_list):
    result = {}

    for line in shopping_list.splitlines():
        if line != '':
            parts = line.split(' ')
            amount = int(parts[0])
            item = parts[1]
            result[item] = amount

    return result


def shopping_list_file_to_dict(path):
    with open(path, 'r', encoding='utf-8') as file:
        shopping_list = file.read()

    return shopping_list_to_dict(shopping_list)

def test_shopping_list_to_dict():
    print('Tester shopping_list_to_dict... ', end='')
    arg = '2 brød\n3 pizza\n10 poteter\n1 kaffe\n1 ost\n14 epler\n'
    expected = {
        'brød': 2,
        'pizza': 3,
        'poteter': 10,
        'kaffe': 1,
        'ost': 1,
        'epler': 14,
    }
    actual = shopping_list_to_dict(arg)
    assert expected == actual
    print('OK')

def test_shopping_list_file_to_dict():
    print('Tester shopping_list_file_to_dict... ', end='')
    expected = {
        'brød': 2,
        'pizza': 3,
        'poteter': 10,
        'kaffe': 1,
        'ost': 1,
        'epler': 13,
    }
    actual = shopping_list_file_to_dict('handleliste.txt')
    assert expected == actual
    print('OK')

if __name__ == '__main__':
    test_shopping_list_to_dict()
    test_shopping_list_file_to_dict()