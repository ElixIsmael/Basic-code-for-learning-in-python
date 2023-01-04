#function that accepts two numbers and an operator as parameters and returns the result of the operation. calculate (addition, subtraction, multiplication and division)

def calculator(num1, num2, operator):
  # performs the calculation
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    return num1 / num2
  else:
    print("Please enter a valid operator (+, -, *, /).")

# test the function
result = calculator(2, 5, '*')
print(result)  

# In this example, the function calculator() performs the multiplication operation when it is called with the arguments 2, 5 and '*'. The result is stored in the result variable and displayed on the screen using the print() command.
