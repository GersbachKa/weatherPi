import time

w = [180,180,180]
b = [0,0,0]
q1 = [
    b,b,w,w,w,w,b,b,
    b,b,w,b,b,w,w,b,
    b,w,w,b,b,w,w,b,
    b,b,b,w,w,w,b,b,
    b,b,b,w,w,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,w,w,b,b,b,
    b,b,b,w,w,b,b,b
]
q2 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
]



def unknownAnimation(sense):

    prev = sense.get_pixels()

    for i in range(10):
        sense.set_pixels(q1)
        time.sleep(0.25)
        sense.set_pixels(q2)
        time.sleep(0.25)

    sense.set_pixels(prev)

    return
