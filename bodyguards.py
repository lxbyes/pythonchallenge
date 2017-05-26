# -*- coding: utf-8 -*-
import re
import string


if __name__ == '__main__':
    s = ''.join([line.rstrip() for line in open('guards.txt')])

    print ''.join(re.findall(r'(?<=[a-z][A-Z]{3})[a-z](?=[A-Z]{3}[a-z])', s))

    print ''.join(re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', s))

    print ''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', s))

    # 匹配三个连续一样字符
    #print map(lambda x: ''.join(x), re.findall(r'([a-zA-Z])(\1{2})', s))