import database as db

def viewBooks():
    books = db.getRecords("books")
    if(len(books) == 0):
        print("There are no books in your library")
        return
    print("Available books are listed below\n")
    print("{:<6} {:<35} {:<25} {:<8}".format('Id','Title','Author','status'))
    
    for book in books:
        print("{:<6} {:<35} {:<25} {:<8}".format(book['id'],book['name'],book['author'],book['status']))

def viewIssued():
    print("All issued books are listed below")
    records = db.getColumn("b.bId,b.title,b.author,ib.issuedTo",
    "books b INNER JOIN issued_books ib ON b.bId = ib.bId")

    print("{:<8} {:<35} {:25} {:25}".format("Id","Title","Author","Issued To"))
    for row in records:
        print("{:<8} {:<35} {:25} {:25}".format(row[0],row[1],row[2],row[3]))

def addBook():
    book = {
        "name":input("Enter name of book:"),
        "author":input("Enter author name:"),
        "status":"Available"
    }
    
    db.addBook(book)

def removeBook():
    id = input("Enter book id to be deleted: ")
    db.deleteRec(f"books where bId={id}")

def issueBook():
    allBid = db.getColumn("bId","books")
    
    # get details from user
    bId = int(input("Enter book id to be issued: "))
    
    status = db.getColumn("status",f"books where bId={bId}")[0][0]
    print(status)
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

    bId = int(input("Enter book id to be submitted:"))
    
    if((bId,) in allBid):
        status = db.getColumn("status",f"books where bId={bId}")[0][0]
        if(status == "Available"):
            print("Can't return:Book was never isued")
            return
        db.deleteRec(f"issued_books where bId={bId}")
        db.updateRec(f"books set status = 'Available' where bId = {bId}")
        print("Book Submitted!!!")
    else:
        print("Book not found in records!!!")
        return
    