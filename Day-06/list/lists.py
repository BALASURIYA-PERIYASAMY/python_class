lst = [10,30,20]
print(lst)

# add a number in the list
lst.append(40)      #Add a Value in Last Position
print("Append: ",lst)
lst.insert(1,15)    #Add a Value in the accurate position by using index  ## insert(index,value)
print("Insert: ",lst)
lst.extend([60,50]) #Add Multiple values in the list
print("Extend: ",lst)

#Removeing the values in the List
print("Remove: ",lst.remove(30)) #remove the particular value in the list
print("pop: ",lst.pop(2))        #Remove the Last value of the LIst
print("pop: ",lst.pop(2))        #Remove the value in the Particular place

#Sorting in the List
print("Sort: ",lst.sort())#Arrenging in Assending Order
print("Sort in Desenting: ",lst.sort(reverse=True))#Arrenge in Desending Order
print("Reverse: ",lst.reverse())#Reverse the List

print(lst.count(10))#Return the Count of that number
print(lst.index(15))#Return the Index of the Number
print(lst.clear())  #Remove all Values in the List  