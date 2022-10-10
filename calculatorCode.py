from replit import clear
from art import logo
"""Add"""
def add(n1, n2):
  return n1 + n2

"""Subtract"""
def subtract(n1, n2):
  return n1 - n2

"""Multiply"""
def multiply(n1, n2):
  return n1 * n2

"""Divide"""
def divide(n1, n2):
  return n1 / n2

operations = {
  '+':add,
  '-':subtract, 
  '*':multiply, 
  '/':divide,
}
def calculator():
  print(logo)
  num1 = float(input('what is the first number:\n'))
   
  for symbol in operations:
   print(symbol)
  
  cont = True
  while cont:
    operation_symbol = input('pick an operation from the line above:\n')
  
    num2 = float(input('what is the second number:\n'))
    cal_fn = operations[operation_symbol]
    
    answer = cal_fn(num1, num2)
    
    print(f'{num1} {operation_symbol} {num2} = {answer}')
    
    cont_cal = input(f'type y to cont cal with  or n to end cal:\n')
    if cont_cal == "y": 
       num1 = answer
      
    elif cont_cal == "n":
      cont = False
      clear()
      calculator()
    else:
      print("invalid input")
      cont = False

calculator()

#operation_symbol = input('pick an operation from the line above:\n')
  
  # num2 = int(input('what is the second number:\n'))
  # cal_fn = operations[operation_symbol]
  
  # answer = cal_fn(num1, num2)
  
  # print(f'{num1} {operation_symbol} {num2} = {answer}')
  
  # cont_cal = input(f'type y to cont cal with  or n to end cal:\n')
