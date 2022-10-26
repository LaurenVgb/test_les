array =[]
for i in range(1,21):
    i = i**2
    array.append(i)
print(array)



nl=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))
