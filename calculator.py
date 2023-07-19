def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def calculator():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /) or 'exit' to quit: ")
            
            if operator.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                break
            
            num2 = float(input("Enter the second number: "))
            
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Please try again.")
                continue
            
            print(f"Result: {num1} {operator} {num2} = {result}")
        except ValueError as e:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
