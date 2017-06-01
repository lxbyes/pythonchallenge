# -*- coding: utf-8 -*-

import xmlrpclib

if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/phonebook.php'
    phonebook = xmlrpclib.Server(url)
    print phonebook.phone('Bert')