# -*- coding: utf-8 -*-

from PIL import Image
from cStringIO import StringIO

if __name__ == '__main__':
    s = open('evil2.gfx', 'rb').read()
    for i in range(5):
        piece = s[i::5]
        im = Image.open(StringIO(piece))
        f = open('%d.%s' % (i, im.format.lower()), 'wb')
        f.write(piece)
        f.close()