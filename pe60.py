import time
def primeListFile(upto,fileName):
    f=open(fileName,"r")
    #print(f.readline().split(", "))
    primeList=[int(string) for string in f.readline().split(", ")]
    if upto >= primeList[-1]+2:
        start=primeList[-1]+2
        for n in range(start,upto,2):
            i=0
            while True:
                i+=1
                if n%primeList[i]==0:
                    break
                if primeList[i]**2>n:
                    primeList.append(n)
                    break
        f=open(fileName,"w")
        f.write(str(primeList)[1:-1])
    f.close()
    return primeList

def comboTotal(combo,primeList):
    total=0
    for i in combo:
        total+=primeList[i]
    return total

def increment(combo,n,primeList):
    combo[-1]+=1
    total=comboTotal(combo,primeList)
    index=len(combo)-1
    while total>n:
        combo[index-1]+=1
        for i in range(index,len(combo)):
            combo[i]=combo[i-1]+1
        index-=1
        #print(index)
        total=comboTotal(combo,primeList)
        if index==0:
            break
    return total

def checkPrimeCat(combo,primeList):
    choose2=((i,j) for i in range(len(combo)) for j in range(i+1,len(combo)))
    for ij in choose2:
        cat1="".join([str(primeList[combo[ij[0]]]),str(primeList[combo[ij[1]]])])
        cat2="".join([str(primeList[combo[ij[1]]]),str(primeList[combo[ij[0]]])])
        if not (int(cat1) in primeList and int(cat2) in primeList):
            return False
    return True

def main60():
    primeList=primeListFile(9000000,"primes.txt")
    catCombos=[(1,)]
    i=3
    fives=[]
    done=False
    while not done:
        toAdd=[]
        for combo in catCombos:
            #print((i,),combo)
            consider=(i,)+combo
            #print(consider)
            if checkPrimeCat(consider,primeList):
                toAdd.append(consider)
                if len(consider)>=3:
                    print(consider)
                    if len(consider)==5:
                        fives.append(consider)
                        print("yay!", comboTotal(consider,primeList))
        catCombos+=toAdd
        catCombos.append((i,))
        #print(i, len(catCombos))
        i+=1
        if i>1000:
            done=True
    for combo in fives:
        print("found it:")
        for i in combo:
            print("i=",i,"prime number:",primeList[i],end=", ")
        print()
        print("total=",comboTotal(combo,primeList))



#[399,153,112,56]
#[519,24,7,3]
#[572,99,3,1]
#[582,112,90,1]
#[610,24,7,3]
#[701,102,86,80]
#[777,18,11,1]
#[822,112,106,90]
#[852,86,6,1]


def main60A():
    primeList=primeListFile(9000000,"primes.txt")
    combo=[3,7,24,519,520]
    while True:
        if checkPrimeCat(combo,primeList):
            print("found it:")
            for i in combo:
                print(i,primeList[i],end=", ")
            print()
            print("total=",comboTotal(combo,primeList))
            break
        combo[-1]+=1
        print(combo[-1], primeList[combo[-1]])



def main60B():
    primeList=primeListFile(9000000,"primes.txt")
    primeSum=81
    done=False
    #combo3=[1,11,18]:[3,37,67]
    #combo3=[1,3,28]:[3,7,109]
    #combo3=[3,7,24]:[7,19,97]
    #combo4=[1,3,28,121]
    #combo4=[1,11,18,351]
    #combo4=[3,7,24,519]
    combo3Set=[]
    while True:
        combo=[1,2,3]
        runDone=False
        while not runDone:
            #print(combo)
            while increment(combo,primeSum,primeList) < primeSum:
                while 2 in combo:
                    increment(combo,primeSum,primeList)
            if comboTotal(combo,primeList)>primeSum:
                runDone=True
            elif comboTotal(combo,primeList)==primeSum and checkPrimeCat(combo,primeList):
                print("found it:")
                for i in combo:
                    print(i,primeList[i],end=", ")
                print()
                print("total=",comboTotal(combo,primeList))
                done=True
                runDone=True
                combo3Set.append(combo.copy())
            else:
                increment(combo,primeSum,primeList)
        #print("sum=",primeSum)
        primeSum+=2
        if len(combo3Set)==10:
            break
    print(combo3Set)

main60()





"""
def sameList(l1,l2):
    if len(l1)!=len(l2):
        return False
    list1=l1.copy()
    list2=l2.copy()
    while len(list1)>0:
        try:
            i=list2.index(list1[0])
        except:
            return False
        list1.pop(0)
        list2.pop(i)
    return True

def chooseDiff(n,m,arr=None):
    if m==1:
        comboList=[]
        for i in range(n):
            comboList.append([i])
        return comboList
    else:
        newList=[]
        if arr==None:
            comboList=chooseDiff(n,m-1)
        else:
            comboList=arr
        for combo in comboList:
            for i in range(n):
                if not i in combo:
                    consider=combo+[i]
                    unique=True
                    for newCombo in newList:
                        if sameList(consider,newCombo):
                            unique=False
                            break
                    if unique:
                        newList.append(consider)
        return newList
def main60():
    def primeCat(combo, primes):
        choose2=chooseDiff(5,2)
        for choice in choose2:
            #print("choice:",choice)
            cat1=str(primes[combo[choice[0]]])+str(primes[combo[choice[1]]])
            cat2=str(primes[combo[choice[1]]])+str(primes[combo[choice[0]]])
            #print(cat1,cat2)
            if not int(cat1) in primes or not int(cat2) in primes:
                return False
        return True

    done=False
    primes=primeList(5000000)
    print(primes)
    #print(primeCat((1,3,28,121),primes))
    #print(primes[1], primes[3], primes[28], primes[121])
    while not done:
        #combos=chooseDiff(30,5)
        for combo in makeCombos5(250):
            print(combo)
            if primeCat(combo,primes):
                solution=combo
                break
                done=True
        print("one while loop")
        break
    for i in solution:
        print("solutions:")
        print(primes[i])
#print(chooseDiff(5,2))

#def allDiff(i,j,k,l,m):
#    return i!=j and i!=k and i!=l and i!=m and j!=k and j!=l and j!=m and k!=l and k!=m and l!=m

def goodCombo(*args):
    if 2 in args:
        return False
    elif 3 in args and 4 in args:
        return False
    elif 1 in args and 5 in args:
        return False
    elif 3 in args and 6 in args:
        return False
    return True
def makeCombos5(n):
    return ((i,j,k,l,m) for i in range(1,n) for j in range(i+1,n) for k in range(j+1,n) for l in range(k+1,n) for m in range(l+1,n) if goodCombo(i,j,k,l,m))
def makeCombos4(n):
    return ((i,j,k,l) for i in range(1,n) for j in range(i+1,n) for k in range(j+1,n) for l in range(k+1,n))

#print(list(makeCombos(20)))
#main60()
"""