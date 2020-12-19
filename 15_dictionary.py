myDict = {
    1 : "Hello",
    2 : "Bye",
    3 : "something",
    4 : "anything",
    5 : {11 : "nested", 22 : "Dictionary"}
}

print(myDict[2])
print(myDict[5])
print(myDict[5][22])

myDict[1] = "Hello 2" 
print(myDict)