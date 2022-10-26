

# Exercise 1
# print the integer 2 through 10 using a "for" loop

from functions&loops.Circles.solution import doubles
from numpy import double


x = [0,1,2,3,4,5,6,7,8,9,10]

#for i in x:
 #   if i >2:
  #      print(i)

# Exercise 2
# print the integer 2 through 10 using a "while" loop
z = 1
while z < 11:
    print(z)
    z=z+ 1
    
    

# Exercise 3



# Call doubles() to double the number 2 three times
def doubles(num):
    return num*2


q = 2

for i in range(0,3):
  q = doubles(q)
  print(q)