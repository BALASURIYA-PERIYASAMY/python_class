## The Error Statement
# x = int(input("Enter Value: "))
# print(10/x)

## Handle the Error by Using try except
# try:
#     x = int(input("Enter Value: "))
#     print(10/x)
# except:
#     print("Values is Not Divisible by Zero")

## After a error line will not executed
# try:
#     x = int(input("Enter Value: "))
#     print(10/x)
#     print("Ok Understand")
# except:
#     print("Values is Not Divisible by Zero")

## Using Finally - it execute always when the error is accures or not
# try:
#     x = int(input("Enter Value: "))
#     print(10/x)
# except:
#     print("Values is Not Divisible by Zero")
# finally:
#     print("The Program Executed")


## Mentioning the errors
try:
    x = int(input("Enter Value: "))
    print(10/x)
except ZeroDivisionError:
    print("Values is Not Divisible by Zero")
finally:
    print("The Program Executed")


## Generic Exceptions xception as e:
try:
    x = int(input("Enter Value: "))
    print(10/x)
except Exception as e:
    print(e,"Error Comes")
finally:
    print("The Program Executed")


