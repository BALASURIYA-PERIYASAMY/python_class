# ex-1
st={10, 30, 20}

print(st.add(40))           #Add the value in the set
print(st.update([50,60]))   #Add a list in the set
print(st.remove(20))        #remove the 20 value in the set
print(st.discard(10))       #
print(st.pop())             #Remove the random last value
print(st.clear())           #remove all values


# ex-2
a={1,2,3}
b={3,4,5}

print(a.union(b))           #Combain two set
print(a.intersection(b))    #Give the Common value only
print(a.difference(b))      #Give the a values is not presernt in b
print(b.difference(a))      #Give the b values is not presernt in a
print(a.symmetric_difference(b))    #Not Show the Common values only difference values will show
