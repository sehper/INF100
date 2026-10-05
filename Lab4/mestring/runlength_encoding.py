def compress(raw_binary):
    result = []
    current = '0'   
    count = 0

    for char in raw_binary:
        if char == current:
            count += 1
        else:
            result.append(count)
            current = char
            count = 1

    result.append(count)
    return result


def decompress(compressed_binary):
    result = ''
    current = '0'

    for count in compressed_binary:
        result += current * count
        current = '1' if current == '0' else '0'

    return result

def test_compress():
    print('Tester compress... ', end='')
    assert([2, 3, 4, 4] == compress('0011100001111'))
    assert([0, 2, 1, 8, 1] == compress('110111111110'))
    assert([4] == compress('0000'))
    print('OK')

def test_decompress():
    print('Tester decompress... ', end='')
    assert('0011100001111' == decompress([2, 3, 4, 4]))
    assert('110111111110' == decompress([0, 2, 1, 8, 1]))
    assert('0000' == decompress([4]))
    print('OK')

test_compress()
test_decompress()