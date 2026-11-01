from smiley import draw_smiley


def main():
    from uib_inf100_graphics.simple import canvas, display

    draw_smiley_grid(canvas, 70, 5)

    display(canvas)


def draw_smiley_line(canvas, y, size, n):
    for i in range(n):
        x = i * size
        draw_smiley(canvas, x, y, size)


def draw_smiley_grid(canvas, size, n):
    for i in range(n):
        y = i * size
        draw_smiley_line(canvas, y, size, n)


if __name__ == '__main__':
    main()