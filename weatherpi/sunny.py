import time

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



def sunAnimation(sense):

    prev = sense.get_pixels()

    for i in range(10):
        sense.set_pixels(sun1)
        time.sleep(0.25)
        sense.set_pixels(sun2)
        time.sleep(0.25)

    sense.set_pixels(prev)

    return
