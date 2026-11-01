def rotate(grid, clockwise):
    if clockwise:
        return [list(row) for row in zip(*grid[::-1])] #oppgaver som dette elsker jeg å ha hatt progmod<3
    else:
        return [list(row) for row in zip(*grid)][::-1]