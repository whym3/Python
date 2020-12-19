a = set()

#adding values to the set
a.add(12)
a.add(13)
a.add(13)
a.add(13)          #this proves set is a pair of non repetitive items
a.add(13)
a.add(15)

#tuples can be added to the sets but not lists and dictionary
a.add((1,2,3,4,5))

#prints length of set 
print(len(a))

#removes the specified value
a.remove(12)

#pops out an elemnts
a.pop()
print(a)