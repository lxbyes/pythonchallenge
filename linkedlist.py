# -*- coding: utf-8 -*-
import requests
import re

if __name__ == '__main__':
    prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    findnothing = re.compile(r'nothing is (\d+)').search
    next = '12345'
    last = next
    while next:
        cur = next
        resp = requests.get(prefix + cur)
        content = resp.content
        if re.match(r'\w+\.html', content):
            print 'http://www.pythonchallenge.com/pc/def/' + content
            break
        ans = findnothing(content)
        if ans:
            next = ans.group(1)
        else:
            next = str(int(cur) / 2)
        print '(%s, %s)-%s' % (cur, next, content)