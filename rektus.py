from random import randint
from person import *
def exist():
    society = [Person(1780, 1670, 0)]
    i = 0
    while i < 49:
        society += [Person(1780, 1670, 0)]
        i += 1
    while i > 0:
        print(society[i].special)
        i -= 1
    global ever
    ever += 50
    return society
def average():
    a = 0
    b = 0
    c = 0
    d = 0
    f = 0
    m = 0
    x = len(society)
    avgn = 0
    avht = 0
    avhl = 0
    while a < x:
        avgn += society[a].special[0]
        a += 1
    avgn = avgn / x
    while b < x:
        if(society[b].special[1] == 1):
            m += 1
            b += 1
        else:
            f += 1
            b += 1
    while c < x:
        avht += society[c].special[2]
        c += 1
    avht = avht / x
    
    while d < x:
        avhl += society[d].special[3]
        d += 1
    avhl = avhl / x
    print("Average Gen: ", round(avgn), ", height:", round(avht), ", health: ", round(avhl), "f:m ratio: ", f, ":", m, ".", ever)
def die():
    a = 0
    lifetime = randint(1, 30)
    while(a < len(society)): 
            if((society[a].special[3] - lifetime) > 0):
                society[a].special[3] -= lifetime
            else:
                try:
                    society.remove(society[a])
                except ValueError:
                    print("problem removing", society[a].special, "@", society[a])
            a += 1
def date():
    a = 0
    pairs = []
    left = list(range(0, len(society)))
    while(a < len(left)):
        x = left[randint(0, len(left) - 1)]
        try:
            left.remove(x)
        except ValueError:
            print("error @", left[x])
        y = left[randint(0, len(left) - 1)]
        try:
            left.remove(y)
        except ValueError:
            print("error @", left[y])
        pairs += [[x, y]]
        a += 2
    return(pairs)
def reproduce(pairs):#, society):
    #society = society
    a = 0
    while(a < len(pairs)):
        if(society[pairs[a][0]].special[1] is not society[pairs[a][1]].special[1]):
            if(society[pairs[a][0]].special[0] == society[pairs[a][1]].special[0]):            
                society.append(Person(society[pairs[a][0]].special[2], society[pairs[a][1]].special[2], society[pairs[a][0]].special[0] + 1))
                global ever
                ever += 1
        else:
            pass
        a+=1
    return(society)
ever = 0
society = exist()
average()   
while True:     
    die()
    couplets = date()
    society = reproduce(couplets)#, society)   
    average()