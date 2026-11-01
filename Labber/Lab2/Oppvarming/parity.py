'''
I filen parity.py, skriv en funksjon parity(x) som har en parameter x, 
og som returnerer Partall hvis x er et partall og Oddetall hvis x er et oddetall. 
Du kan anta i funksjonen at x er et heltall med typen int.'''

def parity(x):
    if (x % 2 == 0) is True:
        return 'Partall'
    else:
        return 'Oddetall'
    
print('Tester parity... ', end='')
assert 'Partall' == parity(0)
assert 'Oddetall' == parity(1) 
assert 'Partall' == parity(42)
assert 'Oddetall' == parity(99)
print('OK')