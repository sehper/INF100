def cross_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum


def nth_cross_sum(n, x):
    count = 0
    number = 0
    while count < n:
        number += 1
        if cross_sum(number) == x:
            count += 1
    return number

def test_cross_sum():
    print('Tester cross_sum... ', end='')
    assert 6 == cross_sum(123)
    assert 7 == cross_sum(34)
    assert 0 == cross_sum(0)
    assert 1 == cross_sum(100)
    print('OK')

def test_nth_cross_sum():
    print('Tester nth_cross_sum... ', end='')
    assert nth_cross_sum(3, 7) == 25
    assert nth_cross_sum(1, 10) == 19
    assert nth_cross_sum(2, 10) == 28
    assert nth_cross_sum(10, 2) == 2000
    print('OK')


test_cross_sum()
test_nth_cross_sum()