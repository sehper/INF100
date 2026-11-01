# smiley.py

def draw_smiley(canvas, x, y, size):
    ''' Draws a smiley face with the given size, where the
    left top corner is in the x, y position. '''
    left = x
    top = y
    right = x + size
    bottom = y + size
    width = size
    height = size
    
    # Face
    canvas.create_oval(left, top, right, bottom, fill='yellow')

    # Eyes
    canvas.create_oval(
        left + 0.30 * width, top + 0.25 * height,
        left + 0.40 * width, top + 0.35 * width,
        fill='black', outline=''
    )
    canvas.create_oval(
        left + 0.60 * width, top + 0.25 * height,
        left + 0.70 * width, top + 0.35 * width,
        fill='black', outline=''
    )

    # Mouth
    canvas.create_line(
        left + 0.30 * width, top + 0.65 * height,
        left + 0.50 * width, top + 0.85 * width,
        left + 0.70 * width, top + 0.65 * height,
        smooth=True, fill='black', width=3
    )

if __name__ == '__main__':
    # Kode i denne blokken utføres ikke dersom filen importers,
    # kun dersom dette er hovedfilen som kjøres.
    from uib_inf100_graphics.simple import canvas, display

    draw_smiley(canvas, 100, 100, 200)
    draw_smiley(canvas, 10, 230, 70)
    
    display(canvas)