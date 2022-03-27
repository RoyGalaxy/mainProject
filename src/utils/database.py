import mysql.connector as mysql
import time
import setupsql

def getRecords(table):
    con = mysql.connect(host='localhost',user="u0_a243",passwd="password",database="library" )

    if(con.is_connected):
        cursor = con.cursor()
    
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()
    res = []
    for row in data:
        res.append({"id":row[0],"name":row[1],"author":row[2],"status":row[3]})
    con.close()
    return res

def getColumn(column,table):
    con = mysql.connect(host='localhost',user="u0_a243",passwd="password",database="library" )

    if(con.is_connected):
        cursor = con.cursor()

    cursor.execute(f"select {column} from {table}")
    data = cursor.fetchall()
    con.close()
    return data

def addBook(book):
    con = mysql.connect(host='localhost',user="u0_a243",passwd="password",database="library" )

    if(con.is_connected):
        cursor = con.cursor()

    cursor.execute(f"INSERT INTO books (title,author,status) values ('{book['name']}','{book['author']}','{book['status']}')")
    con.commit()
    con.close()
    print("Book Added successfully!!!")

def issueBook(issuedBook):
    con = mysql.connect(host='localhost',user="u0_a243",passwd="password",database="library" )
    
    if(con.is_connected):
        cursor = con.cursor()

    cursor.execute(f"INSERT INTO issued_books values ({issuedBook['bId']},\"{issuedBook['issuedTo']}\")")
    con.commit()
    con.close()
    updateRec(f"books SET status='issued' WHERE bId={issuedBook['bId']}")
    print("Book Issued Successfully!!!")

def deleteRec(command):
    con = mysql.connect(host='localhost',user="u0_a243",passwd="password",database="library" )
    
    if(con.is_connected):
        cursor = con.cursor()
    try:
        cursor.execute(f"DELETE FROM {command}")
        con.commit()
        con.close()
        print("Records deleted")
    except:
        print("Error Deleting Record")
        con.close()

def updateRec(command):
    con = mysql.connect(host='localhost',user="u0_a243",passwd="password",database="library" )
    
    if(con.is_connected):
        cursor = con.cursor()
        
        cursor.execute(f"UPDATE {command}")
        con.commit()
        con.close()