import json
from pathlib import Path
from qr2_matrix_completion import set_fixed_fields, set_meta_fields

qr_layout = json.loads(Path("qrv2_layout.json").read_text(encoding="utf-8"))
meta_patterns = qr_layout["meta_patterns"]

def should_flip(row, col, mask_no):
    if mask_no == 0:
        return (row + col) % 2 == 0
    if mask_no == 1:
        return row % 2 == 0
    if mask_no == 2:
        return col % 3 == 0
    if mask_no == 3:
        return (row + col) % 3 == 0
    if mask_no == 4:
        return (row//2 + col//3) % 2 == 0
    if mask_no == 5:
        return (row*col) % 2 + (row*col) % 3 == 0
    if mask_no == 6:
        return ((row*col) % 2 + (row*col) % 3) % 2 == 0
    if mask_no == 7:
        return ((row+col) % 2 + (row*col) % 3) % 2 == 0	

def get_masked_matrix(matrix, mask_no):
    new_matrix = [rad[:] for rad in matrix]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if should_flip(i, j, mask_no):
                new_matrix[i][j] = 1 - matrix[i][j]
    return new_matrix
        
def score_matrix(matrix):
    count = len(matrix) * len(matrix[0])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                count -= 2
    
    return abs(count)

def get_refined_matrix(raw_matrix, error_correction_level, qr_layout):
    candidates = []
    scores = []

    for mask_nr in range(8):
        m = get_masked_matrix(raw_matrix, mask_nr)
        set_fixed_fields(m, qr_layout)
        set_meta_fields(m, error_correction_level, mask_nr, qr_layout)
        candidates.append(m)
        scores.append(score_matrix(m))

    best = scores.index(min(scores))  
    return candidates[best]




