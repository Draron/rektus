import time
import sys
from random import randint
from person import *

def exist():
    society = []
    i = 0
    for i in range(0, gdv_stp):
        society += [Person(gdv_stht_mp, gdv_stht_fp, 0)]
    return society

def average():
    #a = 0   #counter for average geneation     abbreviated as of 03/11/17, variable name still in use
    #b = 0   #counter for female to male ratio  abbreviated as of 07/11/17
    #c = 0   #counter for average height        abbreviated as of 07/11/17
    #d = 0   #counter for average health        abbreviated as of 07/11/17
    global maxhte
    global minhte
    maxgen = society[1].special[0]
    mingen = society[1].special[0]
    maxhtf = 0                      #max height female
    maxhtm = 0                      #max height male
    minhtf = 9999                   #min height female
    minhtm = 9999                   #min height male
    x = len(society)
    f = 0           #number of females (used to determine ftm ratio, also height calculations)
    m = 0           #number of males (used to determine ftm ratio, also height calculations)
    avgn = 0        #average gen temp value
    avht = 0        #average height temp value
    avhtm = 0       #average male height temp value
    avhtf = 0       #average female height temp value
    avhl = 0        #average health temp value
    
    for a in range(0, x):
        avgn += society[a].special[0]
        avht += society[a].special[2]
        avhl += society[a].special[3]

        if(society[a].special[0] > maxgen):
            maxgen = society[a].special[0]
        if(society[a].special[0] < mingen):
            mingen = society[a].special[0]
    
        if(society[a].special[1] == 0):
            f += 1
            avhtf += society[a].special[2]
            if(society[a].special[2] < minhtf):
                minhtf = society[a].special[2]
            if(society[a].special[2] > maxhtf):
                maxhtf = society[a].special[2]
        if(society[a].special[1] == 1):
            m += 1
            avhtm += society[a].special[2]
            if(society[a].special[2] < minhtm):
                minhtm = society[a].special[2]
            if(society[a].special[2] > maxhtm):
                maxhtm = society[a].special[2]

        g = f + m
        g = f / g
        fr = g * 100        #female ratio
        mr = (1 - g) * 100  #male ratio

    avgn = avgn / x
    avhtm = avhtm / m
    avhtml.append(avhtm)
    avhtf = avhtf / f
    avhtfl.append(avhtf)
    avht = avht / x
    avhtl.append(avht)
    avhl = avhl / x

    if(minhte > minhtm):
        minhte = minhtm
    elif(minhte > minhtf):
        minhte = minhtf
    elif(maxhte < maxhtm):
        maxhte = maxhtm
    elif(maxhte < maxhtf):
        maxhte = maxhtf

    if(len(sys.argv) >= 1 and not "noaverage" in sys.argv):
        print("gen min/avg/max:", mingen, "/", round(avgn), "/", maxgen, " | height:", round(avht), " | health:", round(avhl), " | Population ever:", Person.all_ever(), " | currently:", m + f, " | f:m ratio: ", round(fr, 2), ":", round(mr, 2), sep='' ) 
    if(len(sys.argv) > 1 and "htdt" in sys.argv):
        print("male height min/max/avg:", round(minhtm), round(maxhtm), round(avhtm), "female height min/max/avg:", round(minhtf), round(maxhtf), round(avhtf), "overall average:", round(avht), "highest ever:", round(maxhte), "smallest ever:", round(minhte))
    
def die():
    a = 0
    lifetime = randint(gdv_hlmin, gdv_hlmax)        #default: (1, 310) (seems to be the most efficient number for not letting the population explode or die out too fast)
    while(a < len(society)): 
            if((society[a].special[3] - lifetime) > 0):
                society[a].special[3] -= lifetime
            else:
                try:
                    society.remove(society[a])
                except ValueError:
                    print("problem removing", society[a].special, "@", society[a])
            a += 1

def dating():
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

def reproduce(pairs):
    a = 0
    while(a < len(pairs)):
        if(society[pairs[a][0]].special[1] is not society[pairs[a][1]].special[1]):
            if(society[pairs[a][0]].special[0] == society[pairs[a][1]].special[0]):            
                society.append(Person(society[pairs[a][0]].special[2], society[pairs[a][1]].special[2], society[pairs[a][0]].special[0] + 1))
        else:
            pass
        a+=1
    return(society)

def execution_parameters():
    global gdv_stp
    global gdv_hlmin
    global gdv_hlmax
    global gdv_stht_fp
    global gdv_stht_mp
    cnt = True
    if(len(sys.argv) > 1):
        argslst = ""
        for i in range(1,len(sys.argv)):
            argslst += sys.argv[i] + ", "
        if("cpar" in sys.argv):
            print("Custom parameters (leave blank for default)")
            sys.stdout.write("Start Population(default: 50, value: int 0-n)?")
            stpp = input()
            try:
                stpp = int(stpp)
                if(stpp == ''):
                    gdv_stp = 50
                elif(stpp > 0):
                    gdv_stp = stpp
            except:
                print("'", stpp, "'is not a valid parameter, default will be used")
            sys.stdout.write("Average height startfemales (default: 1670, value: int 0-n, recommended 1500-2000)?")
            stpp = input()
            try:
                stpp = int(stpp)
                if(stpp == ''):
                    gdv_stht_fp = 1670
                elif(stpp > 0):
                    gdv_stht_fp = stpp
            except:
                print("'", stpp, "'is not a valid parameter, default will be used")
            sys.stdout.write("Average height startmales (default: 1780, value: int 0-n, recommended 1500-2000)?")
            stpp = input()
            try:
                stpp = int(stpp)
                if(stpp == ''):
                    gdv_stht_mp = 1780
                elif(stpp > 0):
                    gdv_stht_mp = stpp
            except:
                print("'", stpp, "'is not a valid parameter, default will be used")
            sys.stdout.write("Minimal health loss (default: 1, value: int 1-n, recommended 1-n<max health loss)?")
            stpp = input()
            try:
                stpp = int(stpp)
                if(stpp == ''):
                    gdv_hlmin = 1780
                elif(stpp > 0):
                    gdv_hlmin = stpp
            except:
                print("'", stpp, "'is not a valid parameter, default will be used")
            sys.stdout.write("Maximal health loss (default: 310, value: int 1-n, recommended 300-320, consider max health!)?")
            stpp = input()
            try:
                stpp = int(stpp)
                if(stpp == ''):
                    gdv_hlmax = 1780
                elif(stpp > 0):
                    gdv_hlmax = stpp
            except:
                print("'", stpp, "'is not a valid parameter, default will be used")
        sys.stdout.write("rektus will be executed with the following parameters: " + argslst + "continue? [Y/n]")
        choice = input().lower()
        if(choice == '' or choice == 'y'):
            cnt = True
        else:
            cnt = False
    return cnt

""" gdv --> (g)lobal(d)eclared(v)alue_[sample name]"""
gdv_hlmin = 1                       #(h)ealth(l)oss minimum
gdv_hlmax = 310                     #(h)ealth(l)oss maximum
gdv_stp = 50                        #(st)art(p)opulation
gdv_stht_fp = 1670                  #(st)art(h)eigh(t)_(f)emale(p)arent
gdv_stht_mp = 1780                  #(st)art(h)eigh(t)_(m)ale(p)arent
cnt = execution_parameters()        #cnt is used to determine if the user is happy with the parameters of execution
maxhte = 0
minhte = 9999
if cnt:
    society = exist()
    average()   
while cnt:
    pointao = time.perf_counter()
    die()
    pointac = time.perf_counter()
    pointbo = time.perf_counter()
    couplets = dating()
    pointbc = time.perf_counter()
    pointco = time.perf_counter()
    society = reproduce(couplets)
    pointcc = time.perf_counter()
    pointdo = time.perf_counter() 
    average()
    pointdc = time.perf_counter()
    if(len(sys.argv) > 1 and "perf" in sys.argv):
        print("runtime overall:", round(pointdc - pointao, 5), "die:", round(pointac - pointao, 5), "dating:", round(pointbc - pointbo, 5), "reproduce:", round(pointcc - pointco, 5), "average:", round(pointdc - pointdo, 5), "for", len(society), "elements in society[]")