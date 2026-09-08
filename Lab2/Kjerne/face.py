from uib_inf100_graphics.simple import canvas, display

canvas.create_oval(100, 50, 400, 400, fill='coral', outline='black')

canvas.create_polygon(
    130, 80,
    180, 110,
    220, 65,
    260, 105,
    310, 70,
    350, 120,
    390, 150,
    370, 100,
    330, 60,
    270, 45,
    200, 50,
    140, 80,
    fill='black')

canvas.create_oval(155, 160, 205, 220, fill='white', outline='black')
canvas.create_oval(295, 160, 330, 220, fill='white', outline='black')

canvas.create_oval(172, 180, 190, 210, fill='black')
canvas.create_oval(310, 180, 328, 210, fill='black')

canvas.create_polygon(
    250, 200,
    225, 275,
    250, 290,
    275, 275,
    fill='coral',
    outline='black'
)

canvas.create_arc(180, 260, 320, 350, start=180, extent=180, fill = 'black', outline = 'black')

display(canvas)