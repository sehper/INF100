def draw_body(canvas, left, top, right, bottom):
    ''' Draws a pig's body. The body itself will be within the 
    area bounded by (left, top, right, bottom), the tail and
    legs will be outside. '''
    width = right - left
    height = bottom - top

    # Legs 
    canvas.create_rectangle(
        left + width * 0.2, top + height / 2,
        left + width * 0.35, bottom + height / 5,
        fill='pink3'
    )
    canvas.create_rectangle(
        left + width * 0.3, top + height / 2,
        left + width * 0.45, bottom + 1.5 * height / 5,
        fill='pink'
    )
    canvas.create_rectangle(
        left + width * 0.6, top + height / 2,
        left + width * 0.75, bottom + height / 5,
        fill='pink3'
    )
    canvas.create_rectangle(
        left + width * 0.7, top + height / 2,
        left + width * 0.85, bottom + 1.5 * height / 5,
        fill='pink'
    )
    
    # Tail
    canvas.create_line(
        left, top + height / 2,
        left - width / 8, top + height / 4,
        left, top,
    )

    # Body
    canvas.create_oval(left, top, right, bottom, fill='pink')


if __name__ == '__pig_main__':
     from uib_inf100_graphics.simple import canvas, display
     draw_body(canvas, 50, 100, 250, 250)
     draw_body(canvas, 240, 300, 350, 350)
     display(canvas)