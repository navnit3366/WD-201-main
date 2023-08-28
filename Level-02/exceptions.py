try:
    numerator = 10
    denominator = 0  # Change this to see different execution flows
    if denominator > 100:
        raise ValueError("Denominator cannot be greater than 100")
    print("Answer is", numerator / denominator)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Value Error! Denominator Must be < 100")  # Catches the Value Error
except:
    print("Something Happened")
finally:
    print("All operations have been completed")

try:
    numerator = 5
    denominator = 0
    print(numerator / denominator)  # Causes an Exception and moves to the execute block
    print("This is still not printed")
except ZeroDivisionError:
    print("You cannot divide by zero")
print("This line will be printed")
