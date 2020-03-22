try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("The Value 0 is an invalid denominator value")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

    # a ValueError occurs when the numerator and denominator are not valid numbers
    # a ZeroDevisionError occurs when the denominator is the value 0
    # somewhat can.