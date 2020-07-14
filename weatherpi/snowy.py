import time


c = [100,100,100]
b = [0,0,0]
s = [200,200,200]

snow1 = [
    c,c,c,c,c,c,c,c,
    c,b,b,b,c,c,b,s,
    s,b,b,b,b,b,b,b,
    b,b,b,b,b,b,s,b,
    b,s,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,s,b,s,b,b,
    s,s,s,s,s,s,s,s
]
snow2 = [
    c,c,c,c,c,c,c,c,
    c,b,b,s,c,c,b,b,
    b,b,b,b,b,b,b,s,
    s,b,b,b,b,b,b,b,
    b,b,b,b,b,b,s,b,
    b,s,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    s,s,s,s,s,s,s,s
]
snow3 = [
    c,c,c,c,c,c,c,c,
    c,b,b,b,c,c,b,b,
    b,b,b,s,b,s,b,b,
    b,b,b,b,b,b,b,s,
    s,b,b,b,b,b,b,b,
    b,b,b,b,b,b,s,b,
    b,s,b,b,b,b,b,b,
    s,s,s,s,s,s,s,s
]
snow4 = [
    c,c,c,c,c,c,c,c,
    c,s,b,b,c,c,s,b,
    b,b,b,b,b,b,b,b,
    b,b,b,s,b,s,b,b,
    b,b,b,b,b,b,b,s,
    s,b,b,b,b,b,b,b,
    b,b,b,b,b,b,s,b,
    s,s,s,s,s,s,s,s
]
snow5 = [
    c,c,c,c,c,c,c,c,
    c,b,b,b,c,c,s,b,
    b,s,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,s,b,s,b,b,
    b,b,b,b,b,b,b,s,
    s,b,b,b,b,b,b,b,
    s,s,s,s,s,s,s,s
]
snow6 = [
    c,c,c,c,c,c,c,c,
    c,b,b,b,c,c,b,b,
    b,b,b,b,b,b,s,b,
    b,s,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,s,b,s,b,b,
    b,b,b,b,b,b,b,s,
    s,s,s,s,s,s,s,s
]

sleeptime = .2083

def snowAnimation(sense):
    prev = sense.get_pixels()

    for i in range(4):
        sense.set_pixels(snow1)
        time.sleep(sleeptime)
        sense.set_pixels(snow2)
        time.sleep(sleeptime)
        sense.set_pixels(snow3)
        time.sleep(sleeptime)
        sense.set_pixels(snow4)
        time.sleep(sleeptime)
        sense.set_pixels(snow5)
        time.sleep(sleeptime)
        sense.set_pixels(snow6)
        time.sleep(sleeptime)


    sense.set_pixels(prev)

    return
