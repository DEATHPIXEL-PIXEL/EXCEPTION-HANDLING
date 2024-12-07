x=9
y=5
print("i am in tryblock")
try: 
    print(x/y)
    raise ValueError
except:
    print("an error has occured")
finally:
    print("hello")