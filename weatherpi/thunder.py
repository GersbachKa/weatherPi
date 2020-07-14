import time


c = [120,120,120]
b = [0,0,0]
l = [253,208,35]

light1 = [
    c,c,c,c,c,c,c,c,
    c,c,c,c,c,c,c,c,
    b,b,b,c,c,c,c,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
]
light2 = [
    c,c,c,c,c,c,c,c,
    c,c,c,c,c,c,c,c,
    b,b,b,c,l,c,c,b,
    b,b,b,l,l,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
]
light3 = [
    c,c,c,c,c,c,c,c,
    c,c,c,c,c,c,c,c,
    b,b,b,c,l,c,c,b,
    b,b,b,l,l,b,b,b,
    b,b,b,l,b,b,b,b,
    b,b,l,l,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
]
light4 = [
    c,c,c,c,c,c,c,c,
    c,c,c,c,c,c,c,c,
    b,b,b,c,l,c,c,b,
    b,b,b,l,l,b,b,b,
    b,b,b,l,b,b,b,b,
    b,b,l,l,b,b,b,b,
    b,b,l,b,b,b,b,b,
    b,l,l,b,b,b,b,b
]


def thunderAnimation(sense):
    prev = sense.get_pixels()

    for i in range(5):
        sense.set_pixels(light1)
        time.sleep(.6)
        sense.set_pixels(light2)
        time.sleep(0.05)
        sense.set_pixels(light3)
        time.sleep(0.05)
        sense.set_pixels(light2)
        time.sleep(0.05)
        sense.set_pixels(light3)
        time.sleep(0.05)
        sense.set_pixels(light4)
        time.sleep(0.1)
        sense.set_pixels(light3)
        time.sleep(0.05)
        sense.set_pixels(light2)
        time.sleep(0.05)


    sense.set_pixels(prev)
    return

