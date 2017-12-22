#!/usr/bin/env python2

from urllib import urlretrieve

def firstNonBlank(lines):
    for eachline in lines:
        if not eachline.strip():
            continue
        else:
            return eachline


def firstLast(webpage):
    f = open(webpage)
    liens = f.readlines()
    f.close()
    print firstNonBlank(lines),
    liens.reverse()
    print firstNonBlank(lines)


def download(url="http://www", process=firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:            # do some processing
        process(retval)


if __name__ == "__main__":
    download()