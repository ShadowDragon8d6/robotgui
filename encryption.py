import os

#special encryption style 
#its rsa but on a smaller scale
#retrieves values for encryption from secrets
p = int(os.environ['P'])
q = int(os.environ['Q'])
e = 2691379
d = int(os.environ['D'])
n = p*q


# turns strings into integers using ASCII
def chartoascii(strs):
  new = ""
  for a in strs:
    b = ord(a)
    if b >= 100:
      b = b-100
    b = str(b)
    if len(b) == 1:
      b = "0" + b
    new= new +b
  return int(new)

#turns integers back into strings again using ascii
def asciitochar(nums):
  new = ""
  nums = str(nums)
  if len(nums) % 2 == 1:
    nums = "0" + nums
  while nums != "":
    set = nums[:2]
    if int(set) < 27:
      set = chr(int(set) + 100)
    else:
      set = chr(int(set))
    new = new + set
    nums = nums[2:]
  return new
#encrypts the strings into integers
def encrypts(strs):
  strs = chartoascii(strs)
  numz = pow(strs, e, n)
  return numz
#decryptes the integers into strings (not used but useful to have)
def decrypts(num):
  strs = pow(num,d,n)
  strs = asciitochar(strs)
  return strs

