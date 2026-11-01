def remove_children(people):
    for person in people[:]:
        if person['age'] < 18:
            people.remove(person)


def get_adults(people):
    adults = []
    for person in people:
        if person['age'] >= 18:
            adults.append(person)
    return adults

def test_remove_children():
    print('Testing remove_children...', end=' ', flush=True)

    # Test 1
    arg = [
        {'name': 'Ole', 'age': 18},
        {'name': 'Ida', 'age': 12},
        {'name': 'Eva', 'age': 13},
        {'name': 'Liv', 'age': 37},
        {'name': 'Adam', 'age': 8}
    ]
    return_val = remove_children(arg)
    expected = [
        {'name': 'Ole', 'age': 18},
        {'name': 'Liv', 'age': 37}
    ]
    assert return_val is None
    assert expected == arg

    # Test 2
    arg = [
        {'name': 'Per', 'age': 8},
        {'name': 'Pål', 'age': 6},
        {'name': 'Espen', 'age': 3}
    ]
    remove_children(arg)
    expected = []
    assert expected == arg

    print('OK')

def test_get_adults():
    print('Testing get_adults...', end=' ', flush=True)

    # Test 1
    arg = [
        {'name': 'Ole', 'age': 18},
        {'name': 'Ida', 'age': 12},
        {'name': 'Eva', 'age': 13},
        {'name': 'Liv', 'age': 37},
        {'name': 'Adam', 'age': 8}
    ]
    return_val = get_adults(arg)
    expected = [
        {'name': 'Ole', 'age': 18},
        {'name': 'Liv', 'age': 37}
    ]
    assert return_val == expected
    assert arg == [
        {'name': 'Ole', 'age': 18},
        {'name': 'Ida', 'age': 12},
        {'name': 'Eva', 'age': 13},
        {'name': 'Liv', 'age': 37},
        {'name': 'Adam', 'age': 8}
    ]

    # Test 2
    arg = [
        {'name': 'Per', 'age': 8},
        {'name': 'Pål', 'age': 6},
        {'name': 'Espen', 'age': 3}
    ]
    actual = get_adults(arg)
    expected = []
    assert expected == actual

    print('OK')

test_get_adults()
test_remove_children()