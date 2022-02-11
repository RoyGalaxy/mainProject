# Library Management system

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
    time.sleep(1)
    getTask() # Recursive Function

def exitProgram():
    print("Thanks for using our program")
    time.sleep(1)
    sys.exit()

tasks = ("issue","submit","add book","view books","view issued books","delete book","exit")
actions = [issueBook,returnBook,addBook,viewBooks,viewIssued,removeBook,exitProgram]

# initiating app
getTask()