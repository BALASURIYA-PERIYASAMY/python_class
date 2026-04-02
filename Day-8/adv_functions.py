## 1. default Argument Function
print("default Argument")
def fun1(a,b=2):
    print(a)
    print(b)
    return a+b

c=fun1(10)
print(c)
print("\n")

#Example-2
def fun1_1(a=10, b=20):
    print(a)
    print(b)
    return a+b

print("\n")
c=fun1_1(21)
print(c)
print("\n")

c=fun1_1(5,25)
print(c)
print("\n")

c=fun1_1(b=10)
print(c)
print("\n")

## 2. Keyword argument
print("Keyword argument")
def fun2(a, b):
    print("a:", a)
    print("b:", b)

fun2(a=32, b=21)
fun2(b=21, a=32)    #The Order is Not a matter to change the value


def modify(a):
    a=a+10
    print("inside fun: ",a)
    return a
    
a= 5
a=modify(a)
print(a)

## 3. Positional Argument
def fun3(a,b):
    print(a)
    print(b)
    return a+b

c=fun3(12,50)
print(c)

c=fun3(50,12)
print(c)


## 4. Arbitrary Arguments
# using *args, **kwards

#ex-1 of *args
def add1(*args):
    print(type(args))
    return sum(args)
print(add1(1,2,3))
print(add1(1,2,3,40,50))


#ex-2 of **kwargs
def info(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs["name"])
    print(kwargs["age"])
info (name="Prince",age=21)

