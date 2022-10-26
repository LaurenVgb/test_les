
from numpy import False_


def exercise1():
    #pass #write your code here
    teller =0
    for i in array2:
        for k in i:
            teller += k
    print(teller)     


array2 = [[1,2,3],[4,5]]


exercise1()
def exercise2():
    pass #write your code here
    array =[]
    for i in range(1,21):
        x =i**2
        array.append(x)
    print(array)
exercise2()

def exercise3():
    pass #write your code here
    x = 1
    y = 1
    z = 1
    
    if x == y or y == z or x==z:
        sum = 0
        #print(sum)
        #print(True)
    else:
        sum = x + y + z
        #print(False)
       # print(sum)
    return sum
    
    
exercise3()

def exercise4():
    pass #write your code here

    array1 =[1,2,3,4]
    array2 =[5,6,7,8]
    
    array3 = []
    array3.append(array1)
    array3.append(array2)
    #print(array3)
    
    newArray = []
    for i in range(len(array3[1])): #kolom
        teller = 0
        for k in array3:    #rij
            teller += k[i]
        newArray.append(teller)
    print(newArray)
    
exercise4()

def exercise5(array):
    pass #write your code here


    
array = [[1, 3, 1, 1, 4],
         [2, 4, 3, 1, 2],
         [3, 5, 4, 1, 1],
         [4, 6, 2, 1, 4]]

