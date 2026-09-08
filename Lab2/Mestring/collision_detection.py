'''I filen collision_detection.py, skriv en funksjon rectangles_overlap som har åtte parametre 
x1, y1, x2, y2, x3, y3, x4, y4, hvor de fire første parametrene ett hyperrektangel, 
og de fire siste representerer et annet (et hyperrektangel representeres av to motsatte hjørner, 
men vi kan ikke gjøre noen ytterligere antakelser om hvilke hjørner). 
La metoden returnere True dersom rektanglene overlapper hverandre, og False hvis ikke. 
Vi sier at rektanglene overlapper selv om de kun deler ett enkelt punkt.

I filen collision_detection.py, skriv en funksjon circle_overlaps_rectangle 
om har syv parametre x1, y1, x2, y2, xc, yc, rc, hvor de fire første parametrene representerer to 
motstående hjørner i et hyperrektangel, og de tre siste representerer en sirkel sentrert i 
La metoden returnere True dersom sirkelen overlapper rektangelet, og False hvis ikke. 
Dersom sirkelen og rektangelet deler kun ett enkelt punkt regnes det fremdeles som at de er overlappende.
'''

def rectangles_overlap(x1, y1, x2, y2, x3, y3, x4, y4):  #Dette programmet er egt bare point_in_rectangle bare du sjekker begge hjørner
    x1min = min(x1, x2)
    x1max = max(x1, x2)
    y1min = min(y1, y2)
    y1max = max(y1, y2)

    x2min = min(x3, x4)
    x2max = max(x3, x4)
    y2min = min(y3, y4)
    y2max = max(y3, y4)
    
    return x1min <= x2max and x2min <= x1max and y1min <= y2max and y2min <= y1max

'''
så lenge x1min <= x2max and x2min <= x1max and y1min <= y2max and y2min <= y1max er sant vil alltid rektanglene
overlappe, både x og y verdier må stemme
'''

def circle_overlaps_rectangle(x1, y1, x2, y2, xc, yc, rc):
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)

    if xmin <= xc <= xmax:
        xclosest = xc
    elif xc < xmin:
        xclosest = xmin
    elif xc > xmax:
        xclosest = xmax
    
    if ymin <= yc <= ymax:
        yclosest = yc
    elif yc < ymin:
        yclosest = ymin
    elif yc > ymax:
        yclosest = ymax

    if ((xc - xclosest)**2 + (yc - yclosest)**2)**0.5 <= rc:
        return True
    
    return False

'''
jeg finner hvilken x og y verdi som er nærmest x og y for sirkelen, dersom x eller y for sirkelen er inne i 
rektangelet resulterer det at lengden sin retningsvektor for x = 0
'''


def test_rectangles_overlap():
    print('Tester rectangles_overlap... ', end='')
    assert rectangles_overlap(0, 0, 5, 5, 2, 2, 6, 6) is True # Delvis overlapp
    assert rectangles_overlap(0, 5, 5, 0, 1, 1, 4, 4) is True # Fullstendig overlapp
    assert rectangles_overlap(0, 1, 7, 2, 1, 0, 2, 7) is True # Kryssende rektangler
    assert rectangles_overlap(0, 5, 5, 0, 5, 5, 7, 7) is True # Deler et hjørne
    assert rectangles_overlap(0, 0, 5, 5, 3, 6, 5, 8) is False # Utenfor
    print('OK')

test_rectangles_overlap()


'''   
def test_circle_overlaps_rectangle():
    print('Tester circle_overlaps_rectangle... ', end='')
    assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 2.5, 2) is True # på midten
    assert circle_overlaps_rectangle(0, 5, 5, 0, 8, 3, 2) is False # langt utenfor
    assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 7, 2.01) is True # på kanten
    assert circle_overlaps_rectangle(0, 5, 5, 0, 5.1, 5.1, 1) is True # på hjørnet
    assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 8.99, 5) is True # på hjørnet
    assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 9.01, 5) is False # bare nesten
    print('OK')

test_circle_overlaps_rectangle()
'''