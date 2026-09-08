'''
Opprett en funksjon circles_overlap(x1, y1, r1, x2, y2, r2) i filen circles_overlap.py. 
La funksjonen returnere True dersom to sirkler beskrevet med henholdsvis x1, y1, r1 og x2, y2, r2 overlapper, 
og False hvis ikke.
'''

def circles_overlap(x1, y1, r1, x2, y2, r2):
    l = ((y2 - y1)**2 + (x2 - x1)**2)**0.5  
    
    if l <= r1 + r2:
        return True
    else:
        return False


'''
Finner lengden mellom to punkt og sjekker om radiusene summert er større eller mindre
'''


def test_circles_overlap():
    print('Testing circles_overlap...', end='')

    # Sirkel1 med sentrum (0, 0) og radius 1
    # Sirkel2 med sentrum (1, 1) og radius 1
    # Overlapper
    assert circles_overlap(0, 0, 1, 1, 1, 1) is True

    # Sirkel1 med sentrum (0, 0) og radius 2
    # Sirkel2 med sentrum (4, 1) og radius 2
    # Overlapper ikke
    assert circles_overlap(0, 0, 2, 4, 1, 2) is False

    # Sirkel1 med sentrum (0, 0) og radius 3
    # Sirkel2 med sentrum (5, 0) og radius 2
    # De overlapper hverandre i et enkelt punkt
    assert circles_overlap(0, 0, 3, 5, 0, 2) is True

    assert circles_overlap(0, 0, 3, 0, 6, 2) is False
    print('OK')

test_circles_overlap()