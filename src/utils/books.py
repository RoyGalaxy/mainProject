import database as db

def viewBooks():
    print("\x1b[36mAvailable books are listed below \x1b[0m")
    books = db.getRecords("books")
    print("{:<6} {:<25} {:<15} {:<8}".format('Id','Title','Author','status'))
    print("\x1b[32m",end="")
    for book in books:
        print("{:<6} {:<25} {:<15} {:<8}".format(book['id'],book['name'],book['author'],book['status']))

def viewIssued():
    print("All issued books")

def addBook():
    book = {
        "name":input("Enter name of book: \x1b[32m"),
        "author":input("\x1b[0mEnter author name: \x1b[32m"),
        "status":"Available"
    }
    print("\x1b[0m")
    db.addBook(book)

def removeBook():
    id = input("\x1b[31mEnter book id to be deleted: ")
    db.deleteRec(f"books where bId={id}")
    print("Book Deleted !!!\x1b[0m")

def issueBook():
    allBid = db.getColumn("bId","books")
    
    # get details from user
    bId = int(input("Enter book id to be issued: \x1b[32m"))
    print("\x1b[0m",end="")
    status = db.getColumn("status",f"books where bId={bId}")[0][0]
    if(status=="issued"):
        print("Book already issued by someone")
        return

    if((bId,) in allBid):
        name = input("Enter the name of issuer: ")
        issuedBook = {
            "bId":bId,
            "issuedTo":name
        }
        db.issueBook(issuedBook)
    else:
        print("Invalid Book Id")

def returnBook():
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
        print("\x1b[36mBook Submitted!!!\x1b[0m")
    else:
        print("\x1b[31mBook not found in records!!!\x1b[0m")
        return
    