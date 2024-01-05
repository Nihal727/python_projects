#A simple calculator which prompts the user for input of numbers and the respective arithmetic operation
#Coded by Muhammed Nihal
def add(x, y):   #Funtion to add two numbers
    return x + y

def subtract(x, y): #Function to find the difference of 2 numbers
    return x - y

def multiply(x, y): #Function to find the product of 2 numbers
    return x * y

def divide(x, y): #Function to divide two numbers
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
#block of code which specifies menu and user input
def calculator():
    print("Simple Calculator\n")

    while True:
        print("Operation Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("0. Exit")

        choice = input("Enter choice (0-4): ")

        if choice == "0":
            print("Exiting calculator. Goodbye!")
            break
        elif choice in ("1", "2", "3", "4"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    calculator()
