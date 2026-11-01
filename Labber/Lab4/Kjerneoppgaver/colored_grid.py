def draw_grid(canvas, x1, y1, x2, y2, color_grid):
    rows = len(color_grid)
    cols = len(color_grid[0])

    width = (x2 - x1) / cols
    height = (y2 - y1) / rows

    for row in range(rows):
        for col in range(cols):
            x = x1 + col * width
            y = y1 + row * height
            color = color_grid[row][col]

            canvas.create_rectangle(
                x, y, x + width, y + height,
                fill=color
            )
