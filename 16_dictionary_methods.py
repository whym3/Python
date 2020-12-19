myDict = {
    1 : "Hello",
    2 : "Bye",
    3 : "something",
    4 : "anything",
    5 : {11 : "nested", 22 : "Dictionary"}
}

#prints keys of dictionary
print(myDict.keys()) 

#prints the values of dictionary
print(myDict.values())

#prints (key,values) for all the contents of the dictionary
print(myDict.items())

updateDict = {6 : "pepsi"}

# updates the dictionary with provided values
myDict.update(updateDict)  
print(myDict)

# prints None when key is not found
print(myDict.get(8))