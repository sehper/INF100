def draw_head(canvas, x, y, radius):
    ''' Draws a pig's head centered in (x, y) with radius r. '''
    left = x - radius
    top = y - radius
    right = x + radius
    bottom = y + radius

    draw_ears(canvas, left, top, right, bottom)
    canvas.create_oval(left, top, right, bottom, fill='pink') # Head
    draw_eyes(canvas, x, y, radius)

    # Nose
    nose_left = x - radius / 3
    nose_top = y
    nose_right = x + 2 * radius / 3
    nose_bottom = y + 3 * radius / 5
    draw_nose(canvas, nose_left, nose_top, nose_right, nose_bottom)


def draw_eyes(canvas, x, y, radius):
    ''' Draws the eyes of the pig, assuming the pigs head is
    centered in (x, y) with radius r. '''
    er = radius / 6
    ey = y - radius / 2
    ex_l = x - radius / 4
    ey_r = x + radius / 2
    canvas.create_oval(ex_l - er, ey - er, ex_l + er, ey + er, fill='black')
    canvas.create_oval(ey_r - er, ey - er, ey_r + er, ey + er, fill='black')


def draw_ears(canvas, left, top, right, bottom):
    ''' Draws the pigs ears, assuming the pigs head is within 
    (left, top, right, bottom) '''
    scalar = (bottom - top) 

    # Left ear
    canvas.create_polygon(
        left + scalar * 0.15,
        top + scalar * 0.15,
        left + scalar * 0.22,
        top - scalar * 0.15,
        left + scalar * 0.5,
        top + scalar * 0.1,
        fill='pink',
        outline='black'
    )
    # Right ear
    canvas.create_polygon(
        right - scalar * 0.09,
        top + scalar * 0.21,
        right - scalar * 0.12,
        top - scalar * 0.1,
        right - scalar * 0.5,
        top + scalar * 0.1,
        fill='pink',
        outline='black'
    )


def draw_nose(canvas, left, top, right, bottom):
    ''' Draws a pig nose within the bounds (left, top, right, bottom). '''
    # Main snout
    canvas.create_oval(left, top, right, bottom, fill='lightpink')

    # Nostrils
    r = abs(bottom - top) / 4
    y = (bottom + top) / 2
    xl = (left + right) / 2 - 1.4 * r
    xr = (left + right) / 2 + 1.4 * r
    canvas.create_oval(xl - r, y - r, xl + r, y + r, fill='black')
    canvas.create_oval(xr - r, y - r, xr + r, y + r, fill='black')


if __name__ == '__pig_main__':
     from uib_inf100_graphics.simple import canvas, display
     draw_head(canvas, 200, 150, 100)
     display(canvas)