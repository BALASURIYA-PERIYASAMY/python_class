
'''
Variables is Not Store the Values
it only Store the Object Referense
so the address will Change

Mutable: list, dict, set
Immutablre: int, str, float, tuple

'''

a=10
print(type(a))
print(id(a))

a=a+3
print(id(a))


lst = [1,2]
print(id(lst))
print(id(lst[1]))

lst.append(3)
print(id(lst))
print(id(lst[2]))


a=[1,2]
b=a
print(id(a))
print(id(b))

b=[10,20]
print(id(a))
print(id(b))

print(a)
print(b)

