import json
from pathlib import Path


qr_layout = json.loads(Path("qrv2_layout.json").read_text(encoding="utf-8"))

def set_fixed_fields(matrix, qr_layout):
    for rad, kol in qr_layout['fixed_positions']['zeros']:
        matrix[rad][kol] = 0
    for rad, kol in qr_layout['fixed_positions']['ones']:
        matrix[rad][kol] = 1

def set_meta_fields(matrix, err_corr, mask_no, qr_layout):
    pattern = qr_layout['meta_patterns'][err_corr][mask_no]
    for key in ['first', 'second']:
        positions = qr_layout['meta_positions'][key]
        for bit, (rad, kol) in zip(pattern, positions):
            matrix[rad][kol] = bit





def test_set_fixed_fields():
    print('Testing set_fixed_fields...', end='')
    matrix = [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
    ]
    sample_layout = {
        'about': 'A fake and incomplete QR layout for testing only',
        'side_length': 5,
        'fixed_positions': {
            'zeros': [
                [3, 2], [3, 3], [3, 4], [4, 2], [4, 3], [4, 4]
            ],
            'ones': [
                [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]
            ]
        }
        # skipping keys 'byte_capacity', 'meta_positions' and 'meta_patterns'
        # since they are irrelevant here 
    }
    set_fixed_fields(matrix, sample_layout)
    assert matrix == [
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0],
    ]

    print(' OK')

test_set_fixed_fields()

if __name__ == '__main__':
    from qr_dummies import sample_masked_matrix
    from qr1_draw import display
    from pathlib import Path
    import json

    # Retrieve sample of premasked matrix without meta/fixed fields
    # and getting the matching config for it.
    matrix, error_correction_level, mask_no = sample_masked_matrix()
    qr_layout = json.loads(Path('qrv2_layout.json').read_text(encoding='utf-8'))

    # Try the functions we have created here
    set_meta_fields(matrix, error_correction_level, mask_no, qr_layout)
    set_fixed_fields(matrix, qr_layout)

    # Draw the picture
    display(matrix)