# with open("test.txt","r") as f:
#     print(f.read())

# with open("test.txt","w") as f:
#     f.write("Hello")

# with open("test.txt","a") as f:
#     f.write("\nI am Prince")

# with open("sample1.txt","a") as f:
#     f.write("This is the Sample file for example")

# with open("sample1.txt","r") as f:
#     print(f.read(4))
#     print(f.read(4))


def add_notes():
    note=input("Enter the Note: ")
    with open ("notes.txt","a") as f:
        f.write(note+"\n")

def view_notes():
    with open("notes.txt","r") as f:
        print(f.read())
  
def call():
    add_notes()
    view_notes()

call()   