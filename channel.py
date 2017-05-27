# -*- coding: utf-8 -*-
import re
import zipfile

findnothing = re.compile(r'nothing is (\d+)').search

if __name__ == '__main__':
    z = zipfile.ZipFile('channel.zip', 'r')
    
    next = '90052'
    '''
    while True:
        with open('channel/%s.txt' % next) as f:
            content = f.read()
            result = findnothing(content)
            if result:
                next = result.group(1)
            else:
                print 'Final: %s' % content
                break
            print 'Next: %s-Content: %s' % (next, content)
    '''
    comments = ''
    while True:
        info = z.getinfo('%s.txt' % next)
        content = z.read('%s.txt' % next)
        comments += info.comment
        result = findnothing(content)
        if result:
            next = result.group(1)
        else:
            print 'Final: %s' % content
            break
        print 'Next: %s-Content: %s' % (next, content)
    print comments
