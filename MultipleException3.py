try:
    Value1=int(input("Type the first number:"))
    Value2=int(input("Type the second number:"))
    Output=Value1//Value2
except ValueError:
    print("You muste type a whole number!")
except KeyboardInterrupt:
    print("You pressed Ctrl+C!")
except ZeroDivisionError:
    print("Attempted to divide by zero!")
except ArithmeticError:
    print("An undefined math  error occurred.")
else:
    print(Output)
