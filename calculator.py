# Simple command line calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == "5":
            print("Goodbye!")
            break
        if choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Try again.")
                continue
            if choice == "1":
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif choice == "4":
                try:
                    result = divide(num1, num2)
                except ValueError as e:
                    print(e)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
