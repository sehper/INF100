from uib_inf100_graphics.simple import canvas, display

def draw_marilyn(canvas, x, y, bg_color, face_color):
    # Background
    canvas.create_rectangle(x, y, x+100, y+100, fill = bg_color, outline='')

    # Face
    canvas.create_oval(x+20, y+20, x+80, y+80, outline = face_color, width=2)

    # Eyes
    canvas.create_oval(x+35, y+40, x+45, y+50, fill=face_color, outline='')
    canvas.create_oval(x+55, y+40, x+65, y+50, fill=face_color, outline='')

    # Mouth
    canvas.create_arc(x+35, y+50, x+65, y+70, start=180, extent=180,
                      fill=face_color, outline='')

# Drawing four faces
draw_marilyn(canvas, 50, 50, 'red', 'yellow')
draw_marilyn(canvas, 250, 50, 'blue', 'pink')
draw_marilyn(canvas, 50, 250, 'green', 'purple')
draw_marilyn(canvas, 250, 250, 'cyan', 'orange')

display(canvas)