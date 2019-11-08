# Python 3 
import hashlib
import pyperclip

# list of specials corresponding to shift + number on standard qwerty keyboard
specials = [")", "!", "@", "#", "$", "%", "^", "&", "*", "("]
  
# initializing values
useCaps = input("Use caps? (Y/n) ").lower() or "y"
while(useCaps != "y" and useCaps != "n"):
  print("Only enter Y or N for value.")
  useCaps = input("Use caps? (Y/n) ").lower() or "y"

useSpecial = input("Use special characters? (Y/n) ").lower()  or "y"
while(useSpecial != "y" and useSpecial != "n"):
  print("Only enter Y or N for value.")
  useSpecial = input("Use special characters? (Y/n) ").lower() or "y"

str = input("Enter password: ").strip()
while(len(str) == 0):
  print("Password cannot be blank.")
  str = input("Enter password: ").strip()

site = input("Site to be used on: ").strip()

# encoding using encode() 
# then sending to md5()
# then to hex string 
# then to list for easy manipulation
result = list(hashlib.md5((site+str).encode()).hexdigest())

# if using caps, choose two arbitrary values to make caps
if useCaps == "y":
  num = (3 * len(str)) % 32
  while(result[num].isdigit()):
    num = (num + 1) % 32
  result[num] = result[num].upper()
  num = (7 * num) % 32
  while(result[num].isdigit()):
    num = (num + 1) % 32
  result[num] = result[num].upper()

# if using specials, choose two arbitrary values to make special from above list
if useSpecial == "y":
  num = (2 * len(str)) % 32
  while(not result[num].isdigit()):
    num = (num + 1) % 32
  result[num] = specials[int(result[num])]
  num = (5 * num) % 32
  while(not result[num].isdigit()):
    num = (num + 1) % 32
  result[num] = specials[int(result[num])]

final = "".join(result)
  
# printing the new value.
print("The hashed password is: ", end ="") 
print(final)

copy = input("Copy to clipboard? (Y/n)").lower() or "y"
while(copy != "y" and copy != "n"):
  print("Answer only Y or N")
  copy = input("Copy to clipboard? (Y/n)").lower() or "y"

if copy == "y":
  pyperclip.copy(final)
