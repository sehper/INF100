def is_leap_year(x):
    if x % 400 == 0:
        return True
    elif x % 100 == 0:
        return False
    elif x % 4 == 0:
        return True
    else:
        return False
    
def test_is_leap_year():
    print('Tester is_leap_year... ', end='')
    assert is_leap_year(2022) is False # Ikke delelig med 4
    assert is_leap_year(1996) is True  # Normalt skuddår
    assert is_leap_year(1900) is False # Delbart med 100
    assert is_leap_year(2000) is True  # Delbart med 400
    print('OK')

test_is_leap_year()