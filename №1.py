mass=['a','b','c','d','e','a','a','b','c']
def dict0(mass):
    dict1={}
    for i in mass:
        mass2=[]
        for j in range(len(mass)):
            if mass[j]==i:  
                mass2.append(j)
            dict1[i]=mass2
    return dict1
print(dict0(mass))

dict2 = {i: list(filter(lambda x: mass[x] == i, range(len(mass)))) for i in mass}
print(dict2)
