#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unicodedata import combining, normalize

def noncombining(u):
    """
    >>> normalize('NFKD', 'ä'.decode('UTF-8'))
    u'a\u0308'
    >>> noncombining(u'a')
    True
    >>> noncombining(u'\u0308')
    False
    """
    return not combining(u)

def remove_diacritics(s, encoding='UTF-8'):
    """
    >>> remove_diacritics('áÖèůçŷṫŠ')
    'aOeucytS'
    >>> remove_diacritics('áÖèůçŷṫŠ'.decode('UTF-8'))
    u'aOeucytS'
    """
    if isinstance(s, unicode):
        return filter(noncombining, normalize('NFKD', s))
    else:
        return filter(noncombining,
                      normalize('NFKD', s.decode(encoding))).encode(encoding)

if __name__ == '__main__':
    from doctest import testmod
    testmod()
