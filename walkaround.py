# -*- coding: utf-8 -*-

from PIL import Image

#cat
def spiral(source):
    target = Image.new(source.mode, (100, 100))
    left, top, right, bottom = (0, 0, 99, 99)
    x, y = 0, 0
    dirx, diry = 1, 0
    for i in xrange(10000):
        target.putpixel((x, y), source.getpixel((i, 0)))
        #print source.getpixel((i, 0))
        if dirx == 1 and x == right:
            dirx, diry = 0, 1
            top += 1
        elif dirx == -1 and x == left:
            dirx, diry = 0, -1
            bottom -= 1
        elif diry == 1 and y == bottom:
            dirx, diry = -1, 0
            right -= 1
        elif diry == -1 and y == top:
            dirx, diry = 1, 0
            left += 1
        x += dirx
        y += diry
    return target

#you took the wrong curve. (bit)
def spiral1(source):
    target = Image.new(source.mode, (100, 100))
    x, y = 0, 0
    for i in xrange(10000):
        target.putpixel((x, y), source.getpixel((i, 0)))
        if y == 99:
            x = 0
        else:
            x += 1
        y = (y+1) % 100
    return target


if __name__ == '__main__':
    img = Image.open('wire.png')
    spiral(img).show()