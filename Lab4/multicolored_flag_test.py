from uib_inf100_graphics.simple import canvas, display
from multicolored_flag import draw_multicolored_flag

draw_multicolored_flag(canvas, 125, 135, 275, 265, ["red", "orange", "yellow", "green", "blue", "purple"])
draw_multicolored_flag(canvas, 10, 10, 40, 36, ["black", "yellow", "red"])
draw_multicolored_flag(canvas, 10, 340, 390, 360, ["black", "white", "black","black", "white", "black","black", "white", "black"])

display(canvas)