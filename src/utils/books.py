import database as db

def issueBook(): #Modified
    allBid = db.getColumn("bId","books")
    bId = int(input("Enter book id to be issued: \x1b[32m"))
    print("\x1b[0m",end="")
    if((bId,) in allBid):
        status = db.getColumn("status",f"books where bId={bId}")[0][0]
        if(status=="issued"):
            print("Book already issued by someone")
            return
        name = input("Enter the name of issuer: ")
        db.addRecord("issued_books",f"{bId},'{name}'")
        db.updateRec(f"books SET status='issued' where bId={bId}")
        db.saveChanges(); #save changes to mysql
        print("\x1b[36mBook Issued successfully\x1b[0m")
    else:
        print("Invalid Book Id")

def returnBook(): #Modified
    allBid = db.getColumn("bId","books")
    bId = int(input("Enter book id to be issued: \x1b[32m"))
    print("\x1b[0m",end="")
    if((bId,) in allBid):
        status = db.getColumn("status",f"books where bId={bId}")[0][0]
        if(status == "Available"):
            print("Can't return:Book was never isued")
            return
        db.deleteRec(f"issued_books where bId={bId}")
        db.updateRec(f"books set status = 'Available' where bId = {bId}")
        db.saveChanges(); #save changes to mysql
        print("\x1b[36mBook Submitted!!!\x1b[0m")
    else:
        print("\x1b[31mBook not found in records!!!\x1b[0m")
        return

def addBook(): #Modified
    name = input("Enter name of book: \x1b[32m")
    author = input("\x1b[0mEnter author name: \x1b[32m")
    db.addRecord("books (title,author,status)",f"'{name}','{author}','Available'")
    print("Book Addded Successfully!!!\x1b[0m")
    db.saveChanges(); #save changes to mysql

def viewBooks(): #Modified
    books = db.getRecords("books")
    print("{:<6} {:<35} {:<25} {:<8}".format('Id','Title','Author','status'))
    print("\x1b[32m",end="")
    for book in books:
        print("{:<6} {:<35} {:<25} {:<8}".format(book[0],book[1],book[2],book[3]))

def viewIssued():
    books = db.getRecords("issued_books ib INNER JOIN books b on ib.bId = b.bId")
    print("{:<6} {:35} {:25} {:20}".format("Id","Title","Author","Issuer"))
    print("\x1b[32m",end="")
    for book in books:
        print("{:<6} {:35} {:25} {:20}".format(book[0],book[3],book[4],book[1]))

def removeBook():
    id = input("\x1b[31mEnter book id to be deleted: ")
    db.deleteRec(f"books where bId={id}")
    print("Book Deleted !!!\x1b[0m")
    db.saveChanges(); #save changes to mysql