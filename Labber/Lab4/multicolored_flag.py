def draw_multicolored_flag(canvas, x1, y1, x2, y2, colors):
    width = (x2 - x1) / len(colors)

    for i in range(len(colors)):
        canvas.create_rectangle(
            x1 + i * width,
            y1,
            x1 + (i + 1) * width,
            y2,
            fill=colors[i],
            outline=""
        )
