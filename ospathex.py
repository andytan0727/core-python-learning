#!/usr/bin/env python2

import os

for tmpdir in ('/tmp', r'c:\temp'):
    if os.path.isdir(tmpdir):
        break
    else:
        print 'no temp directory available'
        tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print '*** Current working directory'
    print cwd

    print '*** Creating example directory...'
    oldwd = cwd
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print '*** new working directory'
    print cwd
    print '*** original working listing'
    print os.listdir(oldwd)

    print '*** Creating test file...'
    fobj = open('test', 'w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print '*** Updated directory listing'
    print os.listdir(cwd)

    print "*** Renaming 'test' to 'filetest.txt'"
    os.rename('test', 'filetest.txt')
    print '*** Updated directory listing:'
    os.listdir(cwd)

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print '*** full file pathname'
    print path

    print '*** (pathname, basename) == '
    print os.path.split(path)
    print '*** (filename, extension) == '
    print os.path.split(os.path.basename(path))

    print '*** displaying file contents: '
    fobj = open(path)
    for eachline in fobj:
        print eachline,
    fobj.close()

    print '** deleting test file'
    os.remove(path)
    print '** updated directory listing'
    print os.listdir(cwd)
    os.chdir(os.pardir)
    print '** deleting test directory'
    os.rmdir('example')
    print '** DONE'