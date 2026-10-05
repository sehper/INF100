from copy import deepcopy
from labyrinth import rotate


def run_all():
    test_rotate_3x3()
    test_rotate_5x2_2x5()  
    test_rotate_2x2()
    test_rotate_1x1()


def do_test(go_clockwise, grid, expected):
    print('.', end='')
    grid_org = deepcopy(grid)
    actual = rotate(grid, go_clockwise)

    assert grid_org == grid, (
        f'Unexpected mutation detected. Argument was first {grid_org}, '
        f'but is now {grid} ({go_clockwise=})'
    )

    assert expected == actual, (
        f'For arguments ({go_clockwise=}, {grid=}) we expected {expected} '
        f'but got {actual}.'
    )


def test_rotate_3x3():
    print('Testing rotate with 3x3 matrix', end='')
    do_test(
        go_clockwise=True,
        grid=[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        expected=[
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ],
    )
    do_test(
        go_clockwise=False,
        grid=[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        expected=[
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7],
        ],
    )
    print(' OK')


def test_rotate_5x2_2x5():
    print('Testing rotate with 5x2 matrix', end='')
    do_test(
        go_clockwise=True,
        grid=[
            ['a', 'b'],
            ['c', 'd'],
            ['e', 'f'],
            ['g', 'h'],
            ['i', 'j']
        ],
        expected=[
            ['i', 'g', 'e', 'c', 'a'],
            ['j', 'h', 'f', 'd', 'b']
        ],
    )
    do_test(
        go_clockwise=True,
        grid=[
            ['i', 'g', 'e', 'c', 'a'],
            ['j', 'h', 'f', 'd', 'b']
        ],
        expected=[
            ['j', 'i'],
            ['h', 'g'],
            ['f', 'e'],
            ['d', 'c'],
            ['b', 'a']
        ],
    )
    do_test(
        go_clockwise=False,
        grid=[['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'], ['i', 'j']],
        expected=[['b', 'd', 'f', 'h', 'j'], ['a', 'c', 'e', 'g', 'i']],
    )
    print(' OK')


def test_rotate_2x2():
    print('Testing rotate with 2x2 matrix', end='')
    do_test(True, [['a', 'b'], ['c', 'd']], [['c', 'a'], ['d', 'b']])
    do_test(False, [['a', 'b'], ['c', 'd']], [['b', 'd'], ['a', 'c']])
    print(' OK')


def test_rotate_1x1():
    print('Testing rotate with 1x1 matrix', end='')
    do_test(True, [['a']], [['a']])
    do_test(False, [['a']], [['a']])
    print(' OK')


if __name__ == '__main__':
    run_all()