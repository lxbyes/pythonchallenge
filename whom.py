# -*- coding: utf-8 -*-

from datetime import *

def isleep(year):
    d = date(year, 3, 1)
    return (d - timedelta(days=1)).day == 29

if __name__ == '__main__':
    for year in range(1006, 2000, 10):
        if isleep(year) and date(year, 1, 26).weekday() == 0:
            print year

from calendar import weekday, isleap
print filter(lambda y: isleap(y) and weekday(y, 1, 26) == 0, range(1006, 2000, 10))[-2]