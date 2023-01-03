#simple calculator in Python that can perform the four basic operations (addition, subtraction, multiplication and division)

def calculator():
  while True:
    # get user expression
    expression = input("Digite a expressão (ou digite 'q' para sair): ")
    
    # if the user wants to exit, we end the loop
    if expression == 'q':
      break
    
    # evaluates the expression and prints the result
    result = eval(expression)
    print(result)
    
# start the calculator
calculator()

#Warning: using the eval() function to evaluate user-entered expressions can be dangerous, as it evaluates any Python code passed as an argument. This means that the user could enter an expression that executes malicious or unexpected code. For example, the user could enter the expression

#'__import__("os").system("rm -rf /")'

#which would erase all files on the system. Therefore, it is important to be careful when using the function eval().

#If you want to create a calculator that only evaluates simple math expressions, a safer option would be to use the ast library to evaluate the expression. 

#Here is an example of how to do this:

import ast

def calculator():
