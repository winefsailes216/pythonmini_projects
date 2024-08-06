def display_prompt():
  print("""
      This is a CALCULATOR
      [+] for Addition
      [-] for Subtraction
      [*] for Multiplication
      [/] for Division
      [q] to quit
      
      
      """)
  
def add_num():
  first_num = int(input("Enter the first number: "))
  second_num = int(input("Enter the second number: "))
  sum = first_num + second_num
  print(f"The sum is {sum}") 