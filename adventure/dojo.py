"""
Useful commands:
    ssh - start game
    cd - change directory
    ls - print directories and files
    vim - edit files
    cat - to say if the file is normal
    help - list of commands
    unworm - fix contested file
    logout - quit game
"""

import os
import os.path
from unipath import Path
import random


print """
Well, this game is mostly for playing.
And its under MIT licence.
Have fun.
Fork it.
Sell it.
Bring us beer.
Start with ssh().
"""

goal_url = "/usr/lib"
goal_file = random.choice(list(os.walk(goal_url))[0][2])

current_dir = Path(os.getcwd())
playing = False
virus = goal_url + "/" + goal_file


def ssh():
    global playing
    if not playing:
        playing = True
        print messages[1]
    else:
        print messages[0]
 
 
def logout():
    global playing
    if playing:
        playing = False
        print messages[2]
    else:
        print messages[1]
 
 
def help():
    print globals()["__doc__"]
 
 
def cat(filename):
    global virus
    if filename == virus:
        print messages[7]
 
 
def unworn(filename):
    global virus
    global playing
    if filename == virus:
        print messages[8]
        playing = False
    else:
        print messages[0]
 

def cd(path):
    global current_dir
    if path == '..':
        current_dir = current_dir.parent
    else:
        current_dir = Path(current_dir, path)
    print messages[3] % distance(current_dir, virus)

def pwd():
    global current_dir
    print messages[9] % current_dir

def ls():
    print messages[10] % ", ".join(os.listdir(str(current_dir)))


def distance(curpath, path):
    d = list(Path(curpath).components())
    g = list(Path(path).components())
    for x in d:
        if x in g: g.remove(x)
    a = len(g)
    d = list(Path(curpath).components())
    g = list(Path(path).components())
    for x in g:
        if x in d: d.remove(x)
    b = len(d)
    return a + b


commands = {
    'ssh': ssh,
    'logout': logout,
    'help': help,
}


messages = [
    "That's impossible.",
    ("Oh no!  Your system appears to behave improperly, you little fucker."
     + "  Some lib must have a virus in it!"),
    "You surrendered.  Bye bye",
    "You're %d hops away from that virus, dumbass.",
    "No permissions.  Are you a sudo fucker?",
    "You're too dumb to read that file.",
    "Cannot write to that file, you prick.",
    "Yay! You found the virus!  You're the worst.",
    "YES!  You saved your system!  All the libs are thankful!",
    "You're here dumbass: %s",
    "This is what you have idiot: %s"
]
