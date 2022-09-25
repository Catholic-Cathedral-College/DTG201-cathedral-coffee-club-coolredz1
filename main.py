
from time import sleep

#deffine the menu so I can print the menu with ease and not have to write the whole thing again and again.

#creating a price list
price = [
  "(1)3.00"
  "(2)3.00"
  "(3)3.50"
  "(4)3.00"
  "(5)4.00"
]

def menu (): 
  print("===============================")
  print("|(1)Flat White           $3.00|")
  print("|(2)Cappuccino           $3.00|")
  print("|(3)Latte                $3.50|")
  print("|(4)Decaf                $3.00|")  
  print("|(5)Hot Chocolatte       $4.00|")
  print("|(6)Would like to finish order|")
  print("===============================")
  
#print the title here, then print the menu after it. 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("               BUY MY BROWN DRINK               ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
menu ()

#make an input about what type of coffee they would like 

order = input(print("What type of drink would you like to buy? Please enter in the number for your choice of drink?"))
while order != 0:
  if order == "1":
    print("Flat white has been added to your order")
  elif order == "2":
    print("Cappucino has been added to your order")
  elif order == "3":
    print("Latte has been added to your order")
  elif order == "4":
    print("Decaf has been added to your order")
  elif order == "5":
    print("Hot chocolatte has been added to your order")
  elif order == "6":
    print("order is now ")
  else:
    print("sorry but we do not have that in our menu ")

order = input(print("What type of drink would you like to buy? Please enter in the number for your choice of drink?"))
#Receat process and asking how many coffee they would like to have 

