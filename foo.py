def primeList(upto,primeList=[2,3,5,7,11,13,17,19]):
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
    return primeList

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
    elif 1 in args and 12 in args: 
        return False
    elif 3 in args and 6 in args:
        return False
    elif 3 in args and 8 in args:
        return False
    elif 3 in args and 12 in args:
        return False
    elif 3 in args and 14 in args:
        return False
    return True
def makeCombos5(n):
    return ((i,j,k,l,m) for i in range(3,n) for j in range(i+1,n) for k in range(j+1,n) for l in range(k+1,n) for m in range(l+1,n) if goodCombo(i,j,k,l,m))
def makeCombos4(n):
    return ((i,j,k,l) for i in range(1,n) for j in range(i+1,n) for k in range(j+1,n) for l in range(k+1,n))

#print(list(makeCombos(20)))
main60()