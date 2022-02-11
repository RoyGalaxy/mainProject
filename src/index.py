# Library Management system
# built by Roy Galaxy - 12th student and a web developer

# python libraries
import questionary as qu
import time

# Importing local module files
import os,sys
sys.path.append(os.path.abspath("utils"))

from books import *

def getTask():
    task = qu.select("Please select your task:",choices=tasks).ask()
    index = tasks.index(task)
    actions[index]()
    print()
    # Form self repeating loop
    time.sleep(1)
    getTask()

def performTask():
    if(task in tasks):
        # get user input and perform task accordingly
        i = tasks.index(task)
        actions[i]()
        getTask()
    else:
        print("Not an available feature")

def exitProgram():
    print("Thanks for using our program")
    time.sleep(1)
    sys.exit()

tasks = ("issue","submit","add book","view books","view issued books","delete book","exit")
actions = [issueBook,returnBook,addBook,viewBooks,viewIssued,removeBook,exitProgram]

# Requesting user of task for first time
getTask()