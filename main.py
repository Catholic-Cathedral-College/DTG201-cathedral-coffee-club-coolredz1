
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


def sugar():
  sugar = int(input("would you like sugar with you coffee? "))
  if sugar == "1":
    print("sugar will be added to your coffee ")
  elif sugar == "2":
    print("sugar will not be added to your drink")
  else:
    print("please press [1] for Yes and [2] for No")

#print the title here, then print the menu after it. 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("               BUY MY BROWN DRINK               ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
menu ()

print()

#make an input about what type of coffee they would like 
order = input("What type of drink would you like to buy? Please enter in the number for your choice of drink? ")
print()



while order != 0:
  if order == "1":
    print("Flat white has been added to your order")
    quantity = int(input("How many Flat White(s) would you like to order?"))
    print()
    print(quantity,"Flat White(s) have been added to your order")
    sugar()
    order = input("What type of drink would you like to buy? Please enter in the number for your choice of drink? ")
  elif order == "2":
    print("Cappucino has been added to your order")
    quantity = int(input("How many Cappucino would you like to order? "))
    print()
    print(quantity,"Cappucino(s) has been added to your order.")
    sugar()
    order = input("What type of drink would you like to buy? Please enter in the number for your choice of drink? ")   
  elif order == "3":
    print("Latte has been added to your order")
    quantity = int(input("how many Latte(s) would you like to order?  "))
    print()
    print(quantity,"Latte(s) has been added to your order  ")
    sugar()
    order = input("What type of drink would you like to buy? Please enter in the number for your choice of drink? ")    
  elif order == "4":
    print("Decaf has been added to your order")
    quantity = int(input("How many Decaf(s) woukd you like to buy? "))
    print()
    print(quantity,"Decaf(s) has been added to your order.")
    sugar()
    order = input("What type of drink would you like to buy? Please enter in the number for your choice of drink? ")
  elif order == "5":
    print("Hot chocolatte has been added to your order")
    quantity = int(input("How many Hot chocolate(s) would you like to be buy? "))
    print()
    print(quantity,"Hot chocolatte(s) has been added to your order")
    sugar()
    order = input("What type of drink would you like to buy? Please enter in the number for your choice of drink? ")
  elif order == "0":
    print("order is now complete ")   
    order = 0
  else:
    print("Please pick one on of the options in our menu")
    order = input("What type of drink would you like to buy? Please enter in the number for your choice of drink? ")

    
#asking the name of the customer for the receipt

name = input("What would be the name for the order? ")
name = input(print("Is your name", name,"? Please press 1 for YES and 2 for NO"))
while name !=0:
  if name == "0":
    print("Thank you for conferming")
    name = 0
  elif name == "2":
    print("Sorry would you mind typing it again please")
    name = input("What would the name be for the order? ")
    name = input("Is your name,", name,"? please press 1 for YES and 2 for NO.")
    name = 0
  else:
    print("sorry invalid choice, please press 1 for YES and 2 for NO")
    name = input("What would be the name for the order? ")
    name = input("Is your name", name,"? Please press 1 for YES and 2 for NO")
    name = 0 


#Receipt process and asking how many coffee they would like to have this will aslo show the total for each of the 
