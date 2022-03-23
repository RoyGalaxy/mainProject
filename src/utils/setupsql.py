import mysql.connector as sql

con = sql.connect(host='localhost',user="u0_a243",passwd="password",database="library" )

if(con.is_connected()):
    cursor = con.cursor()

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

if(('books',) not in tables):
    cursor.execute('''CREATE TABLE books 
    (bId INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(30) NOT NULL,
    author VARCHAR(30) NOT NULL,
    status VARCHAR(15) NOT NULL)''')
    cursor.execute("ALTER TABLE books AUTO_INCREMENT = 1001")

if(('issued_books',) not in tables):
    cursor.execute('''CREATE TABLE issued_books 
    (bId INTEGER PRIMARY KEY,issuedTo VARCHAR(30) NOT NULL,FOREIGN KEY(bId) REFERENCES books(bId))''')

con.close()