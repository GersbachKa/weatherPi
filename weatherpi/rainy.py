from sense_hat import SenseHat
import time

s = SenseHat()

s.set_rotation(90,redraw=False)

prev = s.get_pixels()

c = [100,100,100]
b = [0,0,0]
r = [0,110,180]

rain1 = [
    c,c,c,c,c,c,c,c,
    c,c,c,c,c,b,c,c,
    c,c,c,b,b,b,r,c,
    b,b,b,b,b,b,b,b,
    b,b,b,r,b,b,b,b,
    b,b,b,r,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
]
rain2 = [
    c,c,c,c,c,c,c,c,
    c,c,c,c,c,c,b,c,
    c,c,c,c,b,b,b,b,
    b,r,b,b,b,b,r,b,
    b,b,b,b,b,b,r,b,
    b,b,b,b,b,b,b,b,
    b,b,b,r,b,b,b,b,
    b,b,b,r,b,b,b,b
]
rain3 = [
    c,c,c,c,c,c,c,c,
    c,c,c,c,c,c,c,b,
    b,c,c,c,c,b,b,b,
    b,b,b,b,r,b,b,b,
    b,r,b,b,b,b,b,b,
    b,r,b,b,b,b,r,b,
    b,b,b,b,b,b,r,b,
    b,b,b,b,b,b,b,b
]
rain4 = [
    c,c,c,c,c,c,c,c,
    r,c,c,c,c,c,c,c,
    b,b,c,c,c,c,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,r,b,b,b,
    b,b,b,b,r,b,b,b,
    b,r,b,b,b,b,b,b,
    b,r,b,b,b,b,r,b
]
rain5 = [
    c,c,c,c,c,c,c,c,
    c,b,c,c,c,c,c,c,
    r,b,r,c,c,c,c,b,
    r,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,r,b,b,b,
    b,b,b,b,r,b,b,b
]
rain6 = [
    c,c,c,c,c,c,c,c,
    c,c,b,c,c,c,c,c,
    b,b,b,b,c,c,c,c,
    b,b,r,b,b,b,b,r,
    r,b,r,b,b,b,b,b,
    r,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
]
rain7 = [
    c,c,c,c,c,c,c,c,
    c,c,c,b,c,c,c,c,
    c,b,b,b,b,c,c,c,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,r,
    b,b,r,b,b,b,b,r,
    r,b,r,b,b,b,b,b,
    r,b,b,b,b,b,b,b
]
rain8 = [
    c,c,c,c,c,c,c,c,
    c,c,c,c,b,c,c,c,
    c,c,b,r,b,b,c,c,
    b,b,b,r,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,r,
    b,b,r,b,b,b,b,r
]


sleeptime = .15625

for i in range(4):
    s.set_pixels(rain1)
    time.sleep(sleeptime)
    s.set_pixels(rain2)
    time.sleep(sleeptime)
    s.set_pixels(rain3)
    time.sleep(sleeptime)
    s.set_pixels(rain4)
    time.sleep(sleeptime)
    s.set_pixels(rain5)
    time.sleep(sleeptime)
    s.set_pixels(rain6)
    time.sleep(sleeptime)
    s.set_pixels(rain7)
    time.sleep(sleeptime)
    s.set_pixels(rain8)
    time.sleep(sleeptime)


s.set_pixels(prev)
