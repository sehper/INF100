from uib_inf100_graphics.simple import canvas, display

def draw_belgian_flag(canvas, x1, y1, x2, y2):
    l = x2 - x1
    sx = x1 + l/3       #Hvor på x aksen du vil ha svart
    rx = x2 - l/3       #hvor på x aksen du vil ha rødt
    canvas.create_rectangle(x1, y1, x2, y2, fill = 'yellow')
    canvas.create_rectangle(x1, y1, sx, y2, fill = 'black')
    canvas.create_rectangle(rx, y1, x2, y2, fill = 'red')
    return 
       

'''
dele opp lerretet i 3
'''