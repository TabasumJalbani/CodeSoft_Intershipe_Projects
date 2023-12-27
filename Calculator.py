def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."


def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Cannot calculate modulus with zero divisor."


def floor_divide(x, y):
    if y != 0:
        return x // y
    else:
        return "Error: Cannot perform floor division by zero."


while True:
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Display operation choices
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Floor Division")

        # Get user operation choice
        choice = input("Enter choice (1,2,3,4,5,6): ")

        # Perform calculation based on user choice
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = modulus(num1, num2)
        elif choice == '6':
            result = floor_divide(num1, num2)
        else:
            print("Invalid choice. Please enter a valid operation (1,2,3,4,5,6).")
            continue  # Restart the loop to prompt the user again

        # Display the result
        print("Result: {}".format(result))

        # Ask if the user wants to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            print("Bye Bye... Have a Nice Day Dear...")
            break  # Exit the loop if the user does not want to perform another calculation

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print("An error occurred:", str(e))
