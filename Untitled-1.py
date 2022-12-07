

# Program to generate a random number between 0 and 9

# importing the random module
import random

randomlist = []
for i in range(0,100000):
    n = random.randint(1,100000)
    randomlist.append(n)
print(randomlist)
with open('smth.txt', 'w') as f:
    for line in randomlist:
        f.write("%s," % line)