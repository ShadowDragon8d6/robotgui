from tkinter import *
from tkinter import messagebox
import sqlite3
import random


from loginmenu import *
from encryption import *



global crsr
def create():
  #establishes connection
  connection = sqlite3.connect("yes.db")
  
  
  crsr = connection.cursor()
  #creates table 
  sql_command = """CREATE TABLE IF NOT EXISTS emp ( 
  Key INTEGER PRIMARY KEY, 
  fname VARCHAR(20), 
  lname VARCHAR(30), 
  user VARCHAR(30), 
  pass VARCHAR(30));"""

  crsr.execute(sql_command)
  connection.commit()
  
  connection.close()

def close():
  connection = sqlite3.connect("yes.db")
  
  
  crsr = connection.cursor()
  #commits changes and closes connection *very important*

  connection.commit()
  
  connection.close()


#outputs the list of user passwrod pairs (used to see if user password pairs exist)
def checking(user,passw):
  connection = sqlite3.connect("yes.db")
  if passw != "":
    passw = encrypts(passw)
  crsr = connection.cursor()
  crsr.execute("SELECT * FROM emp WHERE user = '{user}' AND pass = '{passw}'".format(user = user,passw = passw))
  ans = crsr.fetchall()
  connection.commit()
  
  connection.close()
  return ans

#checks if key actually exists
def keyy(key):
  connection = sqlite3.connect("yes.db")
  
  
  crsr = connection.cursor()
  crsr.execute("SELECT key FROM emp WHERE key = {key}".format(key=key))
  ans = crsr.fetchall()
  connection.commit()
  
  connection.close()
  return ans
#adds a new user password pair to the database
def inserttion(key,first,last,user,passw):
  connection = sqlite3.connect("yes.db")
  if passw != "":
    passw = encrypts(passw)
  crsr = connection.cursor()
  crsr.execute('INSERT INTO emp VALUES ({key}, "{name}", "{last}", "{user}", "{passw}")'.format(key=key, name=first, last=last, user=user, passw=passw))
  connection.commit()
  
  connection.close()
