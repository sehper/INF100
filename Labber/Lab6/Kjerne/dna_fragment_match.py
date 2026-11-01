import os
directory_of_current_file = os.path.dirname(__file__)
os.chdir(directory_of_current_file)

def best_alignment(genome, sequence):
    best_index = 0
    best_errors = len(sequence)

    for i in range(len(genome) - len(sequence) + 1):
        errors = 0

        for j in range(len(sequence)):
            if genome[i + j] != sequence[j]:
                errors += 1

        if errors < best_errors:
            best_errors = errors
            best_index = i

    return best_index


def best_alignment_to_file(path, sequence):
    with open(path, 'r', encoding='utf-8') as file:
        genome = ''.join(file.read().split())

    return best_alignment(genome, sequence)


def test_best_alignment():
    print('Testing best_alignment...', end='')
    genome = 'AAACACCCCCGGGGGTGTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
    sequence = 'ACACCCCCGGGGATGT'
    assert 2 == best_alignment(genome, sequence)

    genome = 'AAAAAAAAAAAAAAAAACACCCCCGGGGGTGTTTTTTTTTTTTTT'
    sequence =                     'CCGGGGATGT'
    assert 22 == best_alignment(genome, sequence)

    genome = 'TTTAAG'
    sequence = 'AAGT'
    assert 2 == best_alignment(genome, sequence)
    print(' OK')

def test_best_alignment_to_file():
    print('Testing best_alignment_to_file...', end='')
    path = 'human_genome_excerpt.txt'
    assert 30864 == best_alignment_to_file(path, 'AAACAAAGAA')
    assert 2097 == best_alignment_to_file(path, 'GAGTGGGATGAGCCATTGTTCATCT')
    assert 0 == best_alignment_to_file(path, 'TAACCC' * 18)
    assert 49913 == best_alignment_to_file(path, 'CATTTCAGTAGTAATAGGAATCTCCAC')
    print(' OK')

test_best_alignment()
test_best_alignment_to_file()
