
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
order = input("What type of drink would you like to buy? Please enter in the number for your choice of drink? ")
while order != 0:
  if order == "1":
    print("Flat white has been added to your order")
    print("How many Flath white would you like to order?")
    order = 0
  elif order == "2":
    print("Cappucino has been added to your order")
    quantity = input("How many Cappucino would you like to order?")
    print(quantity,"Cappucino(s) has been added to your order.")
    order = 0
  elif order == "3":
    print("Latte has been added to your order")
    order = 0
  elif order == "4":
    print("Decaf has been added to your order")
    order = 0
  elif order == "5":
    print("Hot chocolatte has been added to your order")
    order = 0
  elif order == "6":
    print("order is now complete ")
    order = 0

order = input("What type of drink would you like to buy? Please enter in the number for your choice of drink?")

#asking the name of the customer for the receipt

name = input("What would be the name for the order? ")
name = input("Is your name", name,"? Please press 1 for YES and 2 for NO")
while name !=0:
  if name == "1":
    print("Thank you for conferming")
    name = 0
  elif name == "2":
    print("Sorry would you mind typing it again please")
    name = 0
  else:
    print("sorry invalid choice, please press 1 for YES and 2 for NO")
    name = 0

#Receipt process and asking how many coffee they would like to have 

