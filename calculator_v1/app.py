from display import display_prompt
# from add_num import 
import add_num
from subtract_num import subtract_num
from multiply_num import multiply_num
from divide_num import divide_num


display_prompt()

while True:

  choice = input("Select a process: ")

  if choice == "+":
    add_num.add_num()

  elif choice == "-":
    subtract_num()

  elif choice == "*":
    multiply_num()
    
  elif choice == "/":
    divide_num()
    
  elif choice == "q":
    exit()
    
  elif choice == "help":
    display_prompt()

  else:
    print("I don' understand your command. Please try again")