#!/usr/bin/env python2
import os

db = {}

def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('passed: ')
    db[name] = pwd


def olduser():
    name = raw_input('login: ')
    pwd = raw_input("password: ")
    passwd = db.get(name)
    if passwd == pwd:
        print 'welcome back, %s' %name
    else:
        print 'login incorrect.'

def showmenu():
    prompt = """
[N]ew user login
[E]xisting user login
[Q]uit

Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'

            print '\nYou picked: [%s]' % choice
            if choice not in 'neq':
                print 'Invalid option, try again'
            else:
                chosen = True

        if choice == 'q':
            done = True
        elif choice == 'n':
            newuser()
        else:
            olduser()


if __name__ == '__main__':
    showmenu()
