# -*- coding: utf-8 -*-

#1, 11, 21, 1211, 111221

def genseq(n):
    s = str(n)
    next = ''
    cnt = 0
    cc = s[0]

    for c in s:
        if c == cc:
            cnt += 1
        else:
            next += str(cnt) + cc
            cc = c
            cnt = 1
    next += str(cnt) + cc
    return next

def genseqs(start, n):
    seqs = [start]
    next = start
    for i in range(1, n):
        next = genseq(next)
        seqs.append(next)
    return seqs


if __name__ == '__main__':
    print len(genseqs(1, 31)[30])