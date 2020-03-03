import math
class simplecalculator:
    answer = 0

    def __init__(self):
        pass

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        return num1 / num2
    def square(num1):
        return num1 * num1
    def sqrt(num1):
        return math.sqrt(num1)
if __name__ == "__main__":
    # c = simplecalculator()
    choice = ""
    while choice != "quit":
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Square")
        print("6.Sqrt")
        choice = input("Enter choice:")
        if choice == "6" or choice == "quit":
            break
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter a second number:"))
        if choice == "1":
            print(num1, "+", num2, "=", Calculator.add(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", Calculator.subtract(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", Calculator.multiply(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", Calculator.divide(num1, num2))

        elif choice == '5':
            print(num1, "=", square(num1))

        elif choice == '6':
            print(num1, "=", sqrt(num1))

        else:
            print("Invalid choice")
