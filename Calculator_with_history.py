number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
Operators = input("Enter a operator(+,-,/,*): ")
while True:
    if Operators == "+":
        a = (number1 + number2)
        print(a)
        with open("calculator_history.txt", "a") as f:
            f.write ("\n" + str(f"{number1} + {number2} = {a}"))
        break
    elif Operators == "-":
        a = (number1 - number2)
        print(a)
        with open("calculator_history.txt", "a") as f:
            f.write("\n" + str(f"{number1} - {number2} = {a}"))
        break
    elif Operators == "/":
        a = (number1 / number2)
        print(a)
        with open("calculator_history.txt", "a") as f:
            f.write("\n" + str(f"{number1} / {number2} = {a}"))
        break
    elif Operators == "*":
        a = (number1*number2)
        print(a)
        with open("calculator_history.txt", "a") as f:
            f.write("\n" + str(f"{number1} - {number2} = {a}"))
        break
    else:
        print("invalid Operator")
        Operators = input("Enter a operator(+,-,/,*): ")
        
        
        