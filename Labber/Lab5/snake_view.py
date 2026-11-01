def get_color(value):
    if value == 0:
        return 'lightgray'
    elif value > 0:
        return 'orange'
    else:
        return 'cyan'


def draw_board(canvas, x1, y1, x2, y2, board, info_mode):
    rows = len(board)
    cols = len(board[0])

    cell_width = (x2 - x1) / cols
    cell_height = (y2 - y1) / rows

    for row in range(rows):
        for col in range(cols):
            x_start = x1 + col * cell_width
            y_start = y1 + row * cell_height

            x_end = x_start + cell_width
            y_end = y_start + cell_height

            color = get_color(board[row][col])

            canvas.create_rectangle(
                x_start, y_start, x_end, y_end,
                fill=color,
                outline='white'
            )

            if info_mode:
                canvas.create_text(
                    (x_start + x_end) / 2,
                    (y_start + y_end) / 2,
                    text=f'({row}, {col}) = {board[row][col]}',
                    font=('Arial', 7)
                )
