# Ex-1
list1 = [10, 20, 30]
list2 = list1               #BUG : It not create a copy

list2 = list1.copy()        #This is the Solution

list2.append(99)

print(list1)
print(list2)


# Ex-2
itm = ['apple','banana']

def ad(lst):
    lst.append('cherry')

ad(itm)
print(itm)

# Ex-3
a=10
def f(a):
    a=a+20
f(a)
print(a)