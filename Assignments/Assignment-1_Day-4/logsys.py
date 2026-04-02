username = input("Enter Your Username: ")
password = input("Enter Your Password: ")
secret_code = input("Enter Your Secret_code")

if username == "admin" and password == "pass123" and secret_code == "7777":
    print("Welcome! Login Successful.")
elif username != "admin" and password == "pass123" and secret_code == "7777":
    print("Username Not Found.")
elif username == "admin" and password != "pass123" and secret_code == "7777":
    print("Incorrect Password.")
elif username == "admin" and password == "pass123" and secret_code != "7777":
    print("Wrong Secrat_code. ")
elif username != "admin" and password != "pass123" and secret_code == "7777":
    print("Incorrect Username and Password.")
elif username == "admin" and password != "pass123" and secret_code != "7777":
    print("Incorrect Password and Secret_code.")
elif username != "admin" and password == "pass123" and secret_code != "7777":
    print("Username and Secrat_code Not Found.")
else:
    print("Access Denied")
