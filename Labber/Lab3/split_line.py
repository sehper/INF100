def get_endpoints(i, n, x_lo, x_hi):
    length = (x_hi - x_lo) / n
    start = x_lo + i * length
    end = x_lo + (i + 1) * length
    return start, end


if __name__ == '__main__':
    x_lo = float(input('x_lo = '))
    x_hi = float(input('x_hi = '))
    n = int(input('n = '))

    for i in range(n):
        start, end = get_endpoints(i, n, x_lo, x_hi)
        print(start, end)