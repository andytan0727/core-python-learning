#!/usr/bin/env python2

stack = []


def pushit():
    stack.append(raw_input('Enter new string: ').strip())


def popit():
    stack_size = len(stack)
    if stack_size == 0:
        print 'Cannot pop from an empty stack!'
    else:
        print 'Removed [', repr(stack.pop()), ']'

def viewshow_max_factor():
    print stack  # calls str() internally

CMDs = {'u': pushit, 'o': popit, 'v': viewshow_max_factor}


def showmenu():
    pr = """
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt,IndexError):
                choice = 'q'

            print '\nYou picked [%s] choice' % choice

            if choice not in 'uovq':
                print 'Invalid option. Try again.'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
