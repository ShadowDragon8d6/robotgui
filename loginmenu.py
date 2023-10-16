from tkinter import *
from tkinter import messagebox
import sqlite3
import random

from sql import *
from encryption import *

#opens log in menu
def opens():
  global root
  root = Tk()
  root.geometry("600x400")
  root.title("Log In")
  lable2 = Label(root,text="Welcome! Please login or create an account.")
  lable2.pack()
  lable3 = Label(root,text="")
  lable3.pack()
  addbutton = Button(root,text='Create an Account', command = add)
  addbutton.pack()
  loginbutton = Button(root,text='Login', command = login)
  loginbutton.pack()
  button = Button(root,text='Save and Exit', command = root.destroy)
  button.pack()
  root.mainloop()

#creating username and password screen, prompts user to enter required info

def add():
  root.destroy()
  global create
  create = Tk()
  create.geometry("600x400")
  create.title("Create an Account")
  user = StringVar()
  user2 = StringVar()
  user3 = StringVar()
  b = StringVar()
  lable9 = Label(create,text="Enter your first name:")
  lable9.pack()
  enree9 = Entry(create,textvariable=user2)
  enree9.pack()
  lable90 = Label(create,text="Enter your last name:")
  lable90.pack()
  enree90 = Entry(create,textvariable=user3)
  enree90.pack()
  lable = Label(create,text="Enter a username:")
  lable.pack()
  enree = Entry(create,textvariable=user)
  enree.pack()
  lable2 = Label(create,text="Enter a password:")
  lable2.pack()
  enree2 = Entry(create,textvariable=b,show="*")
  enree2.pack()  
  b = str(b)
  user = str(user)
  crea = Button(create,text="Create Username and Password",command = lambda:checker(enree9,enree90,enree,enree2))
  crea.pack()
  creat = Button(create,text="Exit",command = lambda:exits(create))
  creat.pack()
  create.mainloop()

#creates username and password, checks if key generated is unique and if username and password exists in database
def checker(first,last,user,passw):
  user=str(user.get())
  passw=str(passw.get())
  ans = checking(user,passw)
  
  if ans == []:
    key = random.randrange(100000,999999)
    ans = keyy(key)
    while ans !=[]:
      key = random.randrange(100000,999999)
      ans = keyy(key)
    first=str(first.get())
    last=str(last.get())
    user=str(user)
    passw=str(passw)
    inserttion(key,first,last,user,passw)
    create.destroy()
    messagebox.showinfo('',"A username and password has been created")
    opens()

  else:
    messagebox.showinfo('Error',"Username and Password already exists. Please enter a different password or username.")

#login screen, prompts them to enter user and password

def login():
  root.destroy()
  login = Tk()
  login.geometry("600x400")
  login.title("Log In")
  user = StringVar()
  b = StringVar()
  lable = Label(login,text="Enter your username:")
  lable.pack()
  enree4 = Entry(login,textvariable=user)
  enree4.pack()
  lable2 = Label(login,text="Enter your password:",)
  lable2.pack()
  enree3 = Entry(login,textvariable=b,show="*")
  enree3.pack()
  creater = Button(login,text="Enter",command = lambda:loging(enree4,enree3,login))
  creater.pack()
  creat = Button(login,text="Exit",command = lambda:exits(login))
  creat.pack()
  login.mainloop()
#checker function for login
def loging(enree4,enree3,login):
  username = enree4.get()
  username = str(username)
  password = enree3.get()
  password = str(password)
  ans = checking(username,password)
  if ans != []:
    usermenu(username,password,login)
  else:
    messagebox.showinfo('Error',"Username or Password doesn't exist please try again")

#screen after Loging in

def usermenu(username,password,login):
  login.destroy()
  menus = Tk()
  menus.geometry("600x400")
  ans = checking(username,password)
  print(ans)
  name = ans[0][1] + " " + ans[0][2]
  #welcomes them
  menus.title("WELCOME " + name.upper())

  #moving functions
  def forward():
    log("Move Forward")

  def backward():
    log("Move Backward")

  def left():
    log("Turn Left")

  def right():
    log("Turn Right")

  def stop():
    log("Stop")

  def logout():
    log("Logged Out")
    exits(menus)

  #adds to log
  def log(message):
    current_text = log_label.cget("text") #cget GETS THE CURRENT VALUE
    new_text = f"{message}\n{current_text}"
    log_label.config(text=new_text)



  # Create frames for each part of the grid
  top_left_frame = Frame(menus, width=400, height=300)
  bottomright_frame = Frame(menus, bg="black", width=400, height=300)
  bottom_left_frame = Frame(menus,bg = "blue", borderwidth=2, width=400, height=300)
  top_right_frame = Frame(menus, width=400, height=300)

  top_left_frame.grid(row=0, column=0, sticky="nsew")
  bottomright_frame.grid(row=0, column=1, sticky="nsew")
  bottom_left_frame.grid(row=1, column=0, sticky="nsew")
  top_right_frame.grid(row=1, column=1, sticky="nsew")

  # Places labels and buttons in the frames
  camera_label = Label(top_left_frame, text="CAMERA")
  camera_label.pack()

  log_label = Label(bottomright_frame, text=f"Welcome", fg="white", bg="black", anchor="nw")
  log_label.pack(fill="both", expand=True)


  button_frame = Frame(bottomright_frame, bg="black")
  button_frame.pack(side="bottom", fill="both", expand=True)

  forward_button = Button(top_right_frame, text="   ^   \nForward", command=forward)
  backward_button = Button(top_right_frame, text="Backward\n   v   ", command=backward)
  left_button = Button(top_right_frame, text="<   Left", command=left)
  right_button = Button(top_right_frame, text="Right   >", command=right)
  stop_button = Button(top_right_frame, text="   Stop   ", command=stop)
  logout_button = Button(top_right_frame, text="   Logout   ", command=logout)

  forward_button.grid(row=0, column=1)
  backward_button.grid(row=2, column=1)
  left_button.grid(row=1, column=0)
  right_button.grid(row=1, column=2)
  stop_button.grid(row=1, column=1)
  logout_button.grid(row=2,column=2)

  # Adjust row and column weights to make the grid resizable
  menus.grid_rowconfigure(0, weight=1)
  menus.grid_rowconfigure(1, weight=1)
  menus.grid_columnconfigure(0, weight=1)
  menus.grid_columnconfigure(1, weight=1)

  # Make the log area fill the available space
  bottomright_frame.pack_propagate(False) 
  log_label.pack(fill="both", expand=True)

  menus.mainloop()
  



#helper function for just removing the tks
def exits(h):
  h.destroy()
  opens()