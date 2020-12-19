i = 0
while i<10:
    print("Yes",str(i))
    i+=1

#printing a list using while loop
fruits = ['apple','watermelon','grapes','kiwi']
k=0
while k<len(fruits):
    print(fruits[k])
    k=k+1

# for loop
for item in fruits:
    print(item)

# range function
for i in range(1,8):   #(start,end,step size)
    print(i)

for i in range(0,8,2):     #step of 2
    print(i)


# for loop with else
for i in range(10):         
    print(i)                      #when condition becomes false, then loop goes to else
else:
    print("else block activated")


# Break statement
for i in range(10):
    print(i)
    if i==5:
        break

# Continue statement
for i in range(10):
    if i == 5:                #skips the number 5
        continue
    print(i)


# Pass Statement
i = 4
if i>10:
    pass
print("pass is a none statement it throws no error")

