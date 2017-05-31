# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw

if __name__ == '__main__':
    img = Image.open('cave.jpg')
    coords = []
    for x in range(1, img.size[0], 2):
        for y in range(0, img.size[1], 2):
            coords.append((x, y))
    for x in range(0, img.size[0], 2):
        for y in range(0, img.size[1], 2):
            coords.append((x, y))
    draw = ImageDraw.Draw(img)
    draw.point(coords, fill='black')
    img.save('foo.png')