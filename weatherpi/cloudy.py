import time


c = [193,190,186]
b = [0,0,0]
cloud1 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
]
cloud2 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    c,b,b,b,b,b,b,b,
    c,b,b,b,b,b,b,b,
    c,b,b,b,b,b,b,b,
    c,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
]
cloud3 = [
    b,b,b,b,b,b,b,b,
    b,c,b,b,b,b,b,b,
    c,c,c,b,b,b,b,b,
    c,c,c,b,b,b,b,b,
    c,c,c,b,b,b,b,b,
    c,c,c,b,b,b,b,b,
    c,c,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
]
cloud4 = [
    b,b,b,b,b,b,b,b,
    b,b,b,c,b,b,b,b,
    b,b,c,c,c,b,b,b,
    c,c,c,c,c,b,b,b,
    c,c,c,c,c,b,b,b,
    c,c,c,c,c,b,b,b,
    b,c,c,c,b,b,b,b,
    b,b,b,b,b,b,b,b
]
cloud5 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,c,b,b,
    b,b,b,b,c,c,c,b,
    b,b,c,c,c,c,c,b,
    b,c,c,c,c,c,c,b,
    b,c,c,c,c,c,c,b,
    b,b,b,c,c,c,b,b,
    b,b,b,b,b,b,b,b
]
cloud6 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,c,
    b,b,b,b,b,b,c,c,
    b,b,b,b,c,c,c,c,
    b,b,b,c,c,c,c,c,
    b,b,b,c,c,c,c,c,
    b,b,b,b,b,c,c,c,
    b,b,b,b,b,b,b,b
]
cloud7 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,c,c,
    b,b,b,b,b,c,c,c,
    b,b,b,b,b,c,c,c,
    b,b,b,b,b,b,b,c,
    b,b,b,b,b,b,b,b
]
cloud8 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,c,
    b,b,b,b,b,b,b,c,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
]

sleeptime = .3125

def cloudAnimation(sense):
    prev = sense.get_pixels()

    for i in range(2):
        sense.set_pixels(cloud1)
        time.sleep(sleeptime)
        sense.set_pixels(cloud2)
        time.sleep(sleeptime)
        sense.set_pixels(cloud3)
        time.sleep(sleeptime)
        sense.set_pixels(cloud4)
        time.sleep(sleeptime)
        sense.set_pixels(cloud5)
        time.sleep(sleeptime)
        sense.set_pixels(cloud6)
        time.sleep(sleeptime)
        sense.set_pixels(cloud7)
        time.sleep(sleeptime)
        sense.set_pixels(cloud8)
        time.sleep(sleeptime)


    sense.set_pixels(prev)
    return
