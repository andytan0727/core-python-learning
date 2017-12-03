#!/usr/bin/env python2


def show_max_factor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest factor of %d is %d' % \
                (num, count)
            break
        count -= 1
    else:
        print num, 'is prime'


show_max_factor(133)
