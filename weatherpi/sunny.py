from sense_hat import SenseHat
import time

s = SenseHat()

s.set_rotation(90,redraw=False)

prev = s.get_pixels()

y = [253,184,19]
b = [0,0,0]
sun1 = [
    y,y,y,b,b,b,b,b,
    y,y,y,b,y,y,y,b,
    y,y,b,b,b,b,b,b,
    b,b,b,y,b,b,b,b,
    b,y,b,b,y,b,b,b,
    b,y,b,b,b,y,b,b,
    b,y,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
]
sun2 = [
    y,y,y,b,b,b,b,b,    
    y,y,y,b,b,y,y,y,
    y,y,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,y,b,b,b,
    b,y,b,b,b,y,b,b,
    b,y,b,b,b,b,y,b, 
    b,y,b,b,b,b,b,b
]

for i in range(10):
    s.set_pixels(sun1)
    time.sleep(0.25)
    s.set_pixels(sun2)
    time.sleep(0.25)


s.set_pixels(prev)
