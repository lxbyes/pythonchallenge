# -*- coding: utf-8 -*-
import pickle

if __name__ == '__main__':
    pk_file = open('banner.p', 'rb')
    data = pickle.load(pk_file)

    str = ''

    for list in data:
        print list
        for i in list:
            str += i[0] * i[1]
        str += '\n'
    print str
