# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw

def makeimage(points, name):
    img = Image.new('RGB', (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.point(points, fill=(255,0,0))
    img.save('%s.jpg' % name)
        



if __name__ == '__main__':
    first = []
    second = []
    with open('first.txt', 'r') as ff, open('second.txt', 'r') as fs:
        first = [int(i.strip()) for i in ff.read().split(',')]
        second = [int(i.strip()) for i in fs.read().split(',')]
    first_x = first[::2]
    first_y = first[1::2]
    second_x = second[::2]
    second_y = second[1::2]
    fp = map(lambda i: (first_x[i], first_y[i]), range(len(first_x)))
    sp = map(lambda i: (second_x[i], second_y[i]), range(len(second_x)))
    makeimage(fp, 'first')
    makeimage(sp, 'second')
    fp.extend(sp)
    makeimage(fp, 'bull')