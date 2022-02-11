import mysql.connector as mysql
import time

con = mysql.connect(host='localhost',user="u0_a243",passwd="password",database="library" )
cursor = con.cursor()

def getRecords(table):
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall();
    res = []
    for row in data:
        res.append({"id":row[0],"name":row[1],"author":row[2],"status":row[3]})
    return res;

def getColumn(column,table):
    cursor.execute(f"select {column} from {table}")
    data = cursor.fetchall()
    return data

def addBook(book):
    cursor.execute(f"INSERT INTO books (title,author,status) values ('{book['name']}','{book['author']}','{book['status']}')")
    con.commit()
    print("\x1b[36m\x1b[5mBook Added successfully!!!")
    # time.sleep(3)
    print("\x1b[0m")

def issueBook(issuedBook):
    cursor.execute(f"INSERT INTO issued_books values ({issuedBook['bId']},\"{issuedBook['issuedTo']}\")")
    updateRec(f"books SET status='issued' where bId={issuedBook['bId']}")
    con.commit()
    print("\x1b[36mBook Issued Successfully!!!\x1b[0m")

def deleteRec(command):
    cursor.execute(f"DELETE FROM {command}")
    con.commit()

def updateRec(command):
    cursor.execute(f"UPDATE {command}")
    con.commit();