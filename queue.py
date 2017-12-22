#!/usr/bin/env python

import os

queue = []
def enqueue():
    queue.append(raw_input('Enter new string: ').strip())

def dequeue():
    if len(queue) == 0:
        print 'Cannot dequeue from an empty queue!'
    else:
        print 'Removed [', repr(queue.pop(0)), ']'

def viewqueue():
    print queue  # calls str() internally

CMDs = {'e': enqueue, 'd': dequeue, 'v': viewqueue}

def showmenu():
    pr = """
[E]nqueue
[D]equeue
[V]iew
(Q)uit

Enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt,IndexError):
                choice = 'q'

            print '\nYou picked [%s] choice' % choice

            if choice not in 'edvq':
                print 'Invalid option. Try again.'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
