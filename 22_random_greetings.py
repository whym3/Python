import random

l1 = ["Itachi","Naruto","Sasuke","Madara"]
l2 = ["Hello","Hi","Namaste","Konichiwa"]

for names in l1:
    print(random.choice(l2) , names)