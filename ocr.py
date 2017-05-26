# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = ''.join([line.rstrip() for line in open('ocr.txt')])
    
    oc = {}
    for c in s:
        oc[c] = oc.get(c,0) +1
    
    avg = len(s) // len(oc)

    result = ''.join([x for x in s if oc[x] < avg])

    print result
    