def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        try:
            choice = input("Enter the number of the operation (1/2/3/4/5): ")

            if choice == '5':
                print("Exiting the calculator. Goodbye!")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice, please try again.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"The result is: {num1 + num2}")
            elif choice == '2':
                print(f"The result is: {num1 - num2}")
            elif choice == '3':
                print(f"The result is: {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Division by zero is not allowed.")
                else:
                    print(f"The result is: {num1 / num2}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")


# Run the calculator
if __name__ == "__main__":
    calculator()
