from tkinter import *
from tkinter import messagebox
import os
import pickle 
import random

d={'':{'':900}}



def checker(enree,enree2):
  if create_userpass(enree,enree2) == True:
    save_passuser(enree2,enree)
    create.destroy()
    messagebox.showinfo('',"A username and password has been created")
    opens()

def add():
  root.destroy()
  global create
  create = Tk()
  create.geometry("600x400")
  create.title("Create Username and Password")
  user = StringVar()
  b = StringVar()
  lable = Label(create,text="Enter a username:")
  lable.pack()
  enree = Entry(create,textvariable=user)
  enree.pack()
  lable2 = Label(create,text="Enter a password:\n(must have 8 characters, at least one digit and lower case character):")
  lable2.pack()
  enree2 = Entry(create,textvariable=b)
  enree2.pack()  
  b = str(b)
  user = str(user)
  crea = Button(create,text="Create Username and Password",command = lambda:checker(enree,enree2))
  crea.pack()
  creat = Button(create,text="Exit",command = lambda:exits(create))
  creat.pack()
  create.mainloop()

def create_userpass(enree,enree2):
  user = enree.get()
  user = str(user)
  b = enree2.get()
  b = str(b)
  uservalid = True
  passvalid = False
  if username_exists(user):
    messagebox.showinfo('Error',"Username already exists. Please enter another username.")
  else:
    uservalid = True
  if password_exists(b):
    messagebox.showinfo('Error','Password exists. Please try again')
  else:
    upper = 0
    lower = 0
    digit = 0
    if len(b) < 8:
      messagebox.showinfo('Error','Not valid password. Password length less than 8 characters. Please try again')
    else:
      for n in b:
        if n.isdigit():
          digit = digit +1
        if n.isupper():
          upper = upper +1
        if n.islower():
          lower = lower +1
      if (digit > 0 and lower>0):
        passvalid = True
      else:
        if not (digit) > 0:
          messagebox.showinfo('Error','error not valid password, missing digit, please try again')
        if not (lower > 0):
          messagebox.showinfo('Error','error not valid password, missing lowercase letter, please try again')
    return (passvalid and uservalid)

def password_exists(pas):
  b = False
  if d == {}:
    return False
  else:
    h = d.keys()
    passlist = []
    for a in h:
      g = d[a].keys()
      for z in g:
        passs = z
        passlist.append(passs)
    if h == ():
      return False
    else:
      for a in passlist:
        if a == pas:
          b = True
    return b

def username_exists(user):
  b = False
  h = d.keys()
  h = list(h)
  if h == ():
    return False
  else:
    for a in h:
      if a == user:
        b = True
    return b
    
def save_passuser(enree2,enree):
  user = enree.get()
  user = str(user)
  b = enree2.get()
  b = str(b)
  h = {}
  h[b] = 100
  d[user] = h
  

def withdraw(sb,username,password):
  sb.destroy()
  t = Tk()
  t.geometry("600x400")
  t.title("Deposit or Withdrawals")
  user = IntVar()
  b = IntVar()
  lable = Label(t,text="enter an amount to withdraw:")
  lable.pack()
  global enreee
  enreee = Entry(t,textvariable=user)
  enreee.pack()
  lable2 = Label(t,text="enter an amount to deposit:")
  lable2.pack()
  global enreee2
  enreee2 = Entry(t,textvariable=b)
  enreee2.pack()
  createrss = Button(t,text="Enter",command =lambda:withd(username,password,t))
  createrss.pack()
  creatersss = Button(t,text="Exit",command =lambda:usermenu(username,password,t))
  creatersss.pack()
  t.mainloop()

def withd(username,password,t):
  witha = enreee.get()
  witha = int(witha)
  depos = enreee2.get()
  depos = int(depos)
  mon = d[username][password]
  money = mon + depos - witha
  d[username][password] = money
  messagebox.showinfo('',"You're new balance is $" + str(money))
  t.destroy()
  usemenu(username,password)
  
def games(t,balance,username,password):
  
  if False:
    messagebox.showinfo('ERROR',"Balance is less than $100 (minimum bet). Please deposit more money into your account")
  else:
    t.destroy()
    bet = Tk()
    bet.geometry("600x400")
    bet.title("Higher or Lower")
    lable = Label(bet,text="Please Enter Your Bid (Minimum $0,Maximum $10000)")
    lable.pack()
    user = IntVar()
    enrty = Entry(bet,textvariable=user)
    enrty.pack()
    createrss = Button(bet,text="Enter",command =lambda:game(username,password,enrty,bet))
    createrss.pack()
    creatersss = Button(bet,text="Exit",command =lambda:usermenu(username,password,bet))
    creatersss.pack()
    bet.mainloop()

def game(username,password,bet,be):
  bet = int(bet.get())
  if bet > 10000 or bet <0:
    messagebox.showinfo('Error',"Your bet is greater than $10000 or less than $0")
  else:
    be.destroy()
    start = Tk()
    start.geometry("600x400")
    start.title("Higher or Lower")
    lable = Label(start,text="I will first generate a number between 2-9 inclusive.\nMy next number will be between 1-10 and you will guess if it will be higher or lower.")
    lable.pack()
    numb = random.randrange(2, 10)
    count = 0
    lable3 = Label(start,text="My first number is " + str(numb) +". Will my next number be higher or lower?")
    lable3.pack()
    higher = Button(start,text="Higher",command = lambda:legame(username,password,start,count,numb,bet,1))
    higher.pack()
    lower = Button(start,text="Lower",command = lambda:legame(username,password,start,count,numb,bet,0))
    lower.pack()
    start.mainloop()

def legame(username,password,h,count,number,bet,bools):
  h.destroy()
  game = Tk()
  game.geometry("600x400")
  game.title("Higher or Lower")
  newnum = random.randrange(1, 11)
  while newnum == number:
    newnum = random.randrange(1, 11)
  newnewnum = random.randrange(2, 10)
  if (bools == 0 and number > newnum) or (bools == 1 and number < newnum):
    count = count + 1
    lable = Label(game,text="You are correct! My number was " + str(newnum) + ".")
    lable.pack()
    lable2 = Label(game,text="My next number is " + str(newnewnum) + ".")
    lable2.pack()
    lable3 = Label(game,text="Will my next number be higher or lower?")
    lable3.pack()
    higher = Button(game,text="Higher",command = lambda:legame(username,password,game,count,newnewnum,bet,1))
    higher.pack()
    lower = Button(game,text="Lower",command = lambda:legame(username,password,game,count,newnewnum,bet,0))
    lower.pack()
  else:
    moneyearned = determiner(count,bet)
    lable = Label(game,text="You are incorrect. My number was " + str(newnum) + ".")
    lable.pack()
    lable2 = Label(game,text="Your had a streak of " + str(count) + ".")
    lable2.pack()
    lable3 = Label(game,text="You earned $" + str(moneyearned) + ".")
    lable3.pack()
    money = d[username][password]
    d[username][password] = money - bet + moneyearned
    higher = Button(game,text="Play Again?",command = lambda:games(game,d[username][password],username,password))
    higher.pack()
    lower = Button(game,text="Return to Menu",command = lambda:usermenu(username,password,game))
    lower.pack()
  game.mainloop()

def determiner(count,bet):
  wag = bet
  if (count <= 3):
    wag = 0
  elif (count == 4):
    wag = wag * 0.1
  elif (count == 5):
    wag = wag * 0.4
  elif (count == 6):
    wag = wag * 0.8
  elif (count == 7):
    wag = wag * 1.3
  elif (count == 8):
    wag = wag * 1.8
  elif (count == 9):
    wag = wag * 2.5
  elif (count == 10):
    wag = wag * 3.2
  elif (count >= 11):
    wag = wag * (((count - 11) * .9) + 4)
  return wag

def usermenu(username,password,login):
  login.destroy()
  
  usemenu(username,password)

def usemenu(username,password):
  menus = Tk()
  menus.geometry("600x400")
  menus.title("Higher or Lower")
  money = d[username][password]
  money = str(money)  
  lable = Label(menus,text="Welcome!\nYou have "+money+ " dollars.\n\n")
  lable.pack()
  #creaters = Button(menus,text="Deposit/Withdraw Money",command = lambda:withdraw(menus,username,password))
  #creaters.pack()
  creaters = Button(menus,text="Play Higher or Lower",command = lambda:games(menus,d[username][password],username,password))
  creaters.pack()
  if username == "" and password == "":
    createe = Button(menus,text="Withdraw/Deposit",command = lambda:withdraw(menus,username,password))
    createe.pack()
  creat = Button(menus,text="Log out",command = lambda:exits(menus))
  creat.pack()
  lable2 = Label(menus,text="\n\n\nLeaderboard:")
  lable2.pack()
  lists = sort()
  beans = ""
  if len(lists) < 10:
    bea = len(lists)
  else:
    bea = 10
  for a in range(0,bea):
    beans = beans + "\n" + str(a+1) + ". " + str(lists[a][0])+ "\t$" + str(lists[a][1])
  lable3 = Label(menus,text = beans)
  lable3.pack()
  menus.mainloop()

def exits(h):
  h.destroy()
  opens()

def loging(enree4,enree3,login):
  username = enree4.get()
  username = str(username)
  password = enree3.get()
  password = str(password)
  if username_exists(username):
    if password_exists(password):
      b = StringVar()
      for a in d[username].keys():
        b = a
      if b == password:
        usermenu(username,password,login)
      else:
        messagebox.showinfo('Error',"Username or Password is wrong please try again")
    else:
      messagebox.showinfo('Error',"Username or Password is wrong please try again")
  else:
    messagebox.showinfo('Error',"Username or Password is wrong please try again")

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
  lable2 = Label(login,text="Enter your password:")
  lable2.pack()
  enree3 = Entry(login,textvariable=b)
  enree3.pack()
  creater = Button(login,text="Enter",command = lambda:loging(enree4,enree3,login))
  creater.pack()
  creat = Button(login,text="Exit",command = lambda:exits(login))
  creat.pack()
  login.mainloop()
  
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
  lable2 = Label(root,text="\n\n\nLeaderboard:")
  lable2.pack()
  lists = sort()
  beans = ""
  for a in range(0,len(lists)):
    beans = beans + "\n" + str(a+1) + ". " + str(lists[a][0])+ "\t$" + str(lists[a][1])
  lable3 = Label(root,text = beans)
  lable3.pack()
  root.mainloop()
  
def sort():
  listz = []
  h = d.keys()
  passlist = []
  for a in h:
    g = d[a].keys()
    for z in g:
      passs = z
      passlist.append(passs)
  userlist = d.keys()
  userlist = list(userlist)
  moneylist = []
  for a in range(0,(len(userlist))):
    moneylist.append(d[userlist[a]][passlist[a]])

  for b in range(0,(len(userlist))):
    he = []
    index = biggest(moneylist)
    he.append(userlist[index])
    he.append(moneylist[index])
    listz.append(he)
    userlist.pop(index)
    moneylist.pop(index)
  return listz
  
def biggest(list):
  index = 0
  biggest = list[0]
  for h in range(0,(len(list))):
    if list[h] > biggest:
      biggest = list[h]
      index = h
  return index

if os.path.exists("passfile.txt"):
  f = open('passfile.txt', 'rb')
  d = pickle.load(f)
else:
  f = open("passfile.txt","x")
opens()
f = open('passfile.txt', 'wb')
with f as fh:
  pickle.dump(d, fh)
f.close()

