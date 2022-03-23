# Library Management system
# built by Roy Galaxy - 12th student and a web developer

# python libraries
import time

# Importing local module files
import os,sys
sys.path.append(os.path.abspath("utils"))

from books import *

def getTask():
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")

    choice = int(input("Enter your choice: "))
    print()
    if(choice == 1):
        issueBook()
    elif(choice == 2):
        returnBook()
    elif(choice == 3):
        addBook()
    elif(choice == 4):
        viewBooks()
    elif(choice == 5):
        viewIssued()
    elif(choice == 6): 
        removeBook()
    elif(choice == 7):
        exitProgram()
    
    print()
    # Form self repeating loop
    time.sleep(1)
    getTask()

def exitProgram():
    print("Thanks for using our program")
    time.sleep(1)
    sys.exit()

tasks = ("issue","submit","add book","view books","view issued books","delete book","exit")

# Requesting user of task for first time
getTask()