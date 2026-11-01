def get_next_pos(row, column, size):
    pair = (size - 1 - column) // 2
    right = size - 1 - 2 * pair
    going_up = pair % 2 == 0

    if column == right and right - 1 >= 0:
        return row, column - 1

    if going_up:
        if row > 0:
            return row - 1, right
        return 0, right - 2
    if row < size - 1:
        return row + 1, right
    return size - 1, right - 2


def bit_list_to_raw_matrix(bit_list, qr_layout):
    size = qr_layout["side_length"]

    forbidden = set()
    for key in ("zeros", "ones"):
        for row, col in qr_layout["fixed_positions"][key]:
            forbidden.add((row, col))
    for key in ("first", "second"):
        for row, col in qr_layout["meta_positions"][key]:
            forbidden.add((row, col))

    matrix = [[0] * size for _ in range(size)]
    row, column = size - 1, size - 1
    i = 0
    while i < len(bit_list):
        if not (0 <= row < size and 0 <= column < size):
            raise ValueError("Ikke plass til alle bitene")
        if (row, column) not in forbidden:
            matrix[row][column] = bit_list[i]
            i += 1
        row, column = get_next_pos(row, column, size)
    return matrix