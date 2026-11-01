from uib_inf100_graphics.event_app import run_app
from snake_view import draw_board
import random


def app_started(app):
    app.direction = 'east'
    app.info_mode = True
    app.timer_delay = 300

    app.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    app.snake_size = 3
    app.head_pos = (3, 4)
    app.state = 'active'


def key_pressed(app, event):
    if event.key == 'i':
        app.info_mode = not app.info_mode
        return

    if app.state != 'active':
        return

    if event.key == 'Up':
        app.direction = 'north'
    elif event.key == 'Down':
        app.direction = 'south'
    elif event.key == 'Left':
        app.direction = 'west'
    elif event.key == 'Right':
        app.direction = 'east'
    elif event.key == 'Space':
        move_snake(app)


def timer_fired(app):
    if not app.info_mode and app.state == 'active':
        move_snake(app)


def redraw_all(app, canvas):
    if app.state == 'gameover':
        canvas.create_text(
            app.width / 2,
            app.height / 2,
            text='Game Over',
            font=('Arial', 30)
        )
        return

    draw_board(
        canvas,
        25,
        25,
        app.width - 25,
        app.height - 25,
        app.board,
        app.info_mode
    )

    if app.info_mode:
        canvas.create_text(
            app.width / 2,
            10,
            text=f'Direction: {app.direction}, '
                 f'Size: {app.snake_size}, '
                 f'Head: {app.head_pos}, '
                 f'State: {app.state}',
            font=('Arial', 10)
        )


def get_next_head_position(app):
    row, col = app.head_pos

    if app.direction == 'north':
        row -= 1
    elif app.direction == 'south':
        row += 1
    elif app.direction == 'west':
        col -= 1
    elif app.direction == 'east':
        col += 1

    return (row, col)


def subtract_one_from_all_positives(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] > 0:
                board[row][col] -= 1


def add_apple_at_random_location(grid):
    while True:
        row = random.randrange(len(grid))
        col = random.randrange(len(grid[row]))

        if grid[row][col] == 0:
            grid[row][col] = -1
            return


def is_legal_move(pos, board):
    row, col = pos

    if row < 0 or row >= len(board):
        return False

    if col < 0 or col >= len(board[row]):
        return False

    if board[row][col] > 0:
        return False

    return True


def move_snake(app):
    app.head_pos = get_next_head_position(app)

    row, col = app.head_pos

    if not is_legal_move(app.head_pos, app.board):
        app.state = 'gameover'
        return

    if app.board[row][col] == -1:
        app.snake_size += 1
        add_apple_at_random_location(app.board)
    else:
        subtract_one_from_all_positives(app.board)

    app.board[row][col] = app.snake_size


if __name__ == '__main__':
    run_app(width=500, height=400, title='Snake')
