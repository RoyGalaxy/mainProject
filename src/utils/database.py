import mysql.connector as mysql
import time

con = mysql.connect(host='localhost',user="u0_a243",passwd="password",database="library" )
cursor = con.cursor()

def getRecords(table):
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall();
    return data

def getColumn(column,table):
    cursor.execute(f"select {column} from {table}")
    data = cursor.fetchall()
    return data

def addRecord(table,entry):
    cursor.execute(f"INSERT INTO {table} values ({entry})")

def deleteRec(command):
    cursor.execute(f"DELETE FROM {command}")

def updateRec(command):
    cursor.execute(f"UPDATE {command}")

def saveChanges():
    con.commit()