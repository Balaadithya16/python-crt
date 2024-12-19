try:
    a=int(input("Enter amount:"))
except ValueError:
    print("Enter valid element...")
except ArithmeticError:
    print("please check your internet")
else:
    print("Success")
finally:
    print("Thanks for phonepay")