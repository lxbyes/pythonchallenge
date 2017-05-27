# -*- coding: utf-8 -*-

from PIL import Image
import re

if __name__ == '__main__':
    image = Image.open('oxygen.png')
    dataL = image.convert('L').getdata()
    msg = ''
    for i in range(3, 608, 7):
        msg += chr(dataL[image.size[0]*50+i])
    nums = re.findall(r'\d+', msg)
    result = ''
    for str in nums:
        result += chr(int(str))
    print result