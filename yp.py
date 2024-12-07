try:
    num1=int(input("enter your number : "))
    num2=int(input("enter your number : "))
    result=num1/num2
    print("result is " , result)
except ZeroDivisionError:
    print("cant divide by zero")
except ValueError:
    print("please enter a numerical value")
finally:
    print("bye")