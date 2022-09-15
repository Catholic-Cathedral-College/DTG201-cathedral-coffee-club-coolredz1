
from time import sleep

#deffine the menu so I can print the menu with ease and not have to write the whole thing again and again.

#creating a price list
price = [
  "3.00"
  "3.00"
  "3.50"
  "3.00"
  "4.00"
]

def menu (): 
  print("===============================")
  print("|(1)Flat White           $3.00|")
  print("|(2)Cappuccino           $3.00|")
  print("|(3)Latte                $3.50|")
  print("|(4)Decaf                $3.00|")  
  print("|(5)Hot Chocolatte       $4.00|")
  print("===============================")
  
#print the title here, then print the menu after it. 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("               BUY MY BROWN DRINK               ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
menu ()

#make an input about what type of coffee they would like 

order = input(print("What type of drink would you like to buy? Please enter in the number for your choice of drink.?"))
while order !=0:
  if order == "1":
    print("Flat white has been added to your order")
    order = 0 
  elif order == "2":
    print("Cappucino has been added to your order")
    order = 0
else:
  print("stop")
 
