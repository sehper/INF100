def count_xs(s):
    x = 0
    for i in s:
        if i == "x":
            x += 1
    return x

def test_count_xs():
    print('Tester count_xs... ', end='')
    assert 0 == count_xs('foo bar hei')
    assert 1 == count_xs('x')
    assert 4 == count_xs('xxCoolDragonSlayer99xx')
    print('OK')

test_count_xs()