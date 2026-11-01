def add_asterisks(s):
    words = s.split(';')
    words_with_asterisks = []

    for word in words:
        words_with_asterisks.append('*' + word + '*')

    return ';'.join(words_with_asterisks)


def test_add_asterisks():
    print('Testing add_asterisks...', end='')

    # Test 1
    arg = 'foo;bar;qux'
    actual = add_asterisks(arg)
    expected = '*foo*;*bar*;*qux*'
    assert expected == actual

    # Test 2
    arg = 'honey;mustard'
    actual = add_asterisks(arg)
    expected = '*honey*;*mustard*'
    assert expected == actual

    print('OK')

test_add_asterisks()