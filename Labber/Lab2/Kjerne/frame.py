def frame(text):
    if text.startswith('#'):
        text = '#' + text
    else:
        text = '# ' + text

    if text.endswith('#'):
        return text + ' #'
    return text + ' #'


print('Testing frame... ', end='')
s = 'Carpe diem'
s = frame(s)
assert '## Carpe diem ##' == frame(s)
print('OK')