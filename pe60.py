import time
import math
def primeListFile(upto,fileName):
    try:
        f=open(fileName,"r")
    except:
        f=open(fileName,"w")
        f.write("2, 3, 5, 7, 11")
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

"""
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
"""

def isInList(val,list1):
    for element in list1:
        if val==element:
            return True
        elif element>val:
            return False
    return False

def isPrime(val,primeList):
    if val<10000000:
        return isInList(val,primeList)
    else:
        i=0
        divisor=primeList[i]
        maxDiv=math.ceil(math.sqrt(val))+1
        while divisor <= maxDiv:
            if val%divisor==0:
                return False
            i+=1
            divisor=primeList[i]
        return True


"""
def checkPrimeCat(combo,primeList):
    for i in combo[1:]:
        cat1="".join([str(primeList[combo[[i]]]),str(primeList[combo[0]])])
        cat2="".join([str(primeList[combo[[0]]]),str(primeList[combo[i]])])
        if not isInList(int(cat1), primeList) or not isInList(int(cat2),primeList):
            return False
    return True
"""

def compatible(i,combo,primeList):
    output=[]
    #if i in combo:
    #    return (0,0)
    for n in combo:
        cat1=int(str(primeList[i])+str(primeList[n]))
        if not isPrime(cat1, primeList):
            continue
        cat2=int(str(primeList[n])+str(primeList[i]))
        if not isPrime(cat2, primeList):
            continue
        output.append(n)
    output.append(i)
    #output.sort()
    return output

def four2five(i,combo,primeList):
    for n in combo:
        cat1=int("".join([str(primeList[i]),str(primeList[n])]))
        cat2=int("".join([str(primeList[n]),str(primeList[i])]))
        
        if not isPrime(cat1, primeList) or not isPrime(cat2,primeList):
            return False
    return True

def announce(newCombo,catCombos,fours,fives):
    if len(newCombo)>=4:
        print(newCombo, "length:",len(catCombos))
        if len(newCombo)>=5:
            print("found 5 combo!!!         ", newCombo)
            fives.append(newCombo)
        elif len(newCombo)==4:
            print("found 4 combo:         ", newCombo)
            fours.append(newCombo)


def main60():
    primeList=primeListFile(10000000,"primes.txt")
    fours=[(1, 3, 28, 121), (8, 63, 122, 143), (4, 51, 175, 282), (4, 51, 181, 282), (4, 8, 131, 285), (8, 122, 143, 285), (1, 6, 86, 311), (10, 187, 307, 338), (1, 4, 311, 341), (1, 11, 18, 351), (56, 112, 153, 399), (3, 202, 243, 432), (3, 17, 263, 449), (3, 315, 424, 449), (3, 144, 386, 473), (11, 243, 393, 484), (21, 162, 186, 489), (21, 278, 458, 496), (11, 166, 336, 504), (3, 83, 232, 504), (272, 296, 496, 509), (3, 7, 24, 519), (3, 7, 203, 519), (229, 392, 479, 522), (139, 217, 322, 547), (228, 408, 524, 558), (214, 333, 404, 568), (1, 3, 99, 572), (1, 11, 351, 572), (8, 14, 233, 575), (3, 315, 449, 577), (1, 90, 112, 582), (275, 424, 509, 586), (25, 381, 392, 591), (308, 462, 523, 614), (77, 154, 542, 618), (6, 399, 541, 627), (14, 160, 227, 657), (23, 27, 177, 665), (8, 303, 497, 675), (45, 460, 590, 682), (4, 553, 626, 686), (14, 53, 685, 698), (80, 86, 102, 701), (8, 14, 575, 724), (3, 7, 519, 745), (4, 626, 686, 767), (1, 11, 18, 777), (8, 131, 285, 822), (1, 6, 86, 826), (1, 6, 86, 852), (6, 399, 541, 886), (3, 203, 519, 891), (51, 175, 282, 952), (1, 11, 777, 1005), (4, 8, 285, 1025), (1, 4, 311, 1029), (275, 424, 586, 1057), (6, 399, 627, 1063), (4, 8, 285, 1080), (1, 4, 311, 1090), (14, 233, 575, 1113), (3, 83, 504, 1185), (6, 86, 826, 1222), (1, 11, 351, 1254), (4, 51, 175, 1338), (1, 86, 311, 1711), (1, 11, 572, 1936), (1, 90, 582, 1953), (1, 99, 572, 1982), (1, 11, 572, 1982), (6, 399, 886, 2104), (4, 285, 1080, 2254), (4, 175, 1338, 2342), (3, 28, 121, 2348), (3, 203, 519, 2350), (11, 18, 777, 2355), (4, 51, 1338, 2361), (3, 83, 504, 2438), (1, 112, 582, 2477), (1, 3, 121, 2557), (4, 1080, 2254, 2594), (8, 497, 675, 2604), (1, 3, 2557, 2719), (1, 99, 1982, 2740), (1, 11, 1982, 3059), (3, 83, 1185, 3129), (6, 399, 2104, 3143), (1, 3, 28, 3159), (3, 17, 449, 3159), (3, 28, 2348, 3159), (1, 11, 572, 3311), (11, 1982, 3059, 3614), (3, 28, 121, 3665), (21, 162, 489, 3687), (228, 408, 524, 3732), (4, 181, 282, 3745), (21, 186, 489, 3877), (51, 1338, 2361, 3943), (203, 519, 891, 4054), (203, 519, 2350, 4054), (28, 121, 3665, 4073), (1, 3, 2719, 4087), (6, 399, 1063, 4219), (3, 263, 449, 4235), (272, 296, 496, 4381), (6, 399, 2104, 4483), (3, 83, 3129, 4491), (21, 278, 496, 4563), (45, 460, 682, 4666), (6, 399, 1063, 4877), (1, 11, 1005, 777), (4, 8, 1080, 767), (14, 233, 1113, 739), (6, 86, 1222, 826), (1, 582, 1953, 1447), (6, 399, 2104, 886), (4, 285, 2254, 1080), (4, 175, 2342, 1338), (3, 203, 2350, 1454), (11, 18, 2355, 777), (4, 1338, 2361, 1822), (4, 51, 2361, 1338), (1, 582, 2477, 1178), (1, 3, 2557, 1220), (4, 1080, 2594, 2254), (4, 2254, 2594, 1080), (1, 3, 2719, 2557), (1, 99, 2740, 2523), (1, 99, 2740, 1982), (99, 1982, 2740, 1642), (1, 11, 3059, 1982), (3, 83, 3129, 1185), (6, 399, 3143, 2104), (3, 28, 3159, 2348), (1, 11, 3311, 937), (1, 11, 3311, 843), (11, 1982, 3614, 3059), (11, 3059, 3614, 1982), (21, 186, 3877, 2820), (51, 1338, 3943, 2361), (51, 2361, 3943, 1338), (203, 519, 4054, 2350), (203, 519, 4054, 891), (28, 121, 4073, 3665), (1, 3, 4087, 2719), (3, 2719, 4087, 2184), (6, 399, 4219, 1063), (3, 449, 4235, 1123), (296, 496, 4381, 801), (6, 2104, 4483, 2678), (6, 399, 4483, 2104), (3, 3129, 4491, 4031), (3, 83, 4491, 3129), (3, 3129, 4491, 740), (21, 496, 4563, 3545), (45, 460, 4666, 2064), (6, 1063, 4877, 2678), (6, 399, 4877, 1063), (203, 2350, 1454, 1075), (4, 2361, 1822, 1338), (4, 1338, 1822, 910), (4, 2594, 2254, 1080), (99, 2740, 1982, 1642), (11, 3614, 3059, 1982), (51, 3943, 2361, 1338), (3, 4087, 2719, 2184), (6, 4483, 2678, 2104), (3, 4491, 4031, 3129), (3, 4491, 3129, 740), (21, 496, 3545, 1057), (6, 4877, 2678, 1063), (4, 1822, 1338, 910), (6, 399, 1063, 4877, 4219), (1, 6, 311, 341), (10, 187, 307, 700), (3, 7, 24, 610), (3, 203, 602, 891), (1, 11, 637, 1005), (4, 8, 767, 1080), (1, 42, 311, 1090), (1, 4, 125, 1090), (14, 233, 739, 1113), (1, 582, 1447, 1953), (1, 10, 572, 1982), (11, 572, 643, 1982), (3, 203, 1454, 2350), (4, 1338, 1822, 2361), (1, 582, 1178, 2477), (1, 3, 1220, 2557), (4, 159, 1080, 2594), (99, 1642, 1982, 2740), (1, 99, 2523, 2740), (3, 49, 83, 3129), (1, 11, 393, 3311), (1, 11, 843, 3311), (1, 11, 937, 3311), (21, 186, 2820, 3877), (3, 2184, 2719, 4087), (3, 449, 1123, 4235), (296, 496, 801, 4381), (6, 445, 2104, 4483), (6, 2104, 2678, 4483), (3, 740, 3129, 4491), (3, 3129, 4031, 4491), (21, 496, 3545, 4563), (45, 460, 2064, 4666), (6, 1063, 2678, 4877), (14, 233, 739, 4371), (1, 582, 1447, 1805), (203, 1075, 1454, 2350), (3, 203, 1454, 3704), (4, 53, 1822, 2361), (634, 1338, 1822, 2361), (4, 910, 1338, 1822), (1, 11, 937, 2948), (296, 496, 801, 2514), (21, 496, 1057, 3545), (1063, 2678, 3679, 4877), (6, 1063, 4219, 4877), (129, 203, 1075, 2350), (4, 910, 1822, 3286), (3, 24, 610, 3057), (3, 203, 602, 3704), (1, 637, 1005, 1137), (1, 637, 1005, 2203), (4, 125, 955, 1090), (4, 125, 1090, 1370), (1, 125, 1090, 4813), (1, 10, 572, 4334), (1, 10, 1982, 4795), (3, 49, 83, 2110), (445, 529, 2104, 4483), (14, 739, 4371, 4403), (1, 1447, 1805, 2501), (1, 582, 1805, 2543), (3, 203, 2390, 3704), (3, 203, 2557, 3704), (3, 203, 3704, 3715), (598, 634, 1338, 1822), (634, 1338, 2148, 2361), (129, 203, 1075, 1758), (1, 1005, 1241, 2203), (4, 955, 1090, 4258), (1, 10, 791, 4334), (1, 10, 1464, 4795), (3, 594, 2557, 3704), (3, 3159, 3704, 3715), (3, 203, 3642, 3715), (471, 634, 2148, 2361), (3, 594, 1568, 2557), (3, 1707, 3159, 3715), (3, 3159, 3704, 4543), (6, 471, 634, 2148), (3, 396, 1707, 3715), (1707, 2309, 3159, 3715), (1, 3, 121, 6522), (1, 3, 28, 7807), (4, 51, 181, 5705), (122, 143, 285, 7242), (1, 6, 311, 5744), (6, 86, 311, 7142), (21, 278, 458, 5809), (3, 232, 504, 5427), (3, 203, 519, 8054), (1, 3, 572, 5605), (1, 3, 99, 7331), (1, 3, 99, 8108), (1, 3, 572, 8252), (11, 351, 572, 5669), (14, 233, 575, 7452), (25, 381, 392, 6536), (6, 399, 541, 7951), (8, 303, 497, 5954), (8, 303, 497, 8181), (45, 460, 682, 5260), (4, 626, 686, 6600), (86, 102, 701, 8322), (8, 575, 724, 8317), (1, 18, 777, 5982), (1, 6, 852, 8255), (6, 399, 886, 6037), (3, 519, 891, 6475), (4, 311, 1029, 6062), (1, 351, 1254, 8179), (4, 51, 1338, 6259), (1, 572, 1982, 8252), (3, 121, 2348, 6182), (3, 121, 2348, 7399), (3, 203, 2350, 7012), (4, 51, 2361, 6311), (3, 83, 2438, 6255), (1, 112, 2477, 8326), (1, 3, 2557, 5927), (1, 3, 2719, 5587), (1, 2557, 2719, 6727), (1, 3, 3159, 8108), (1, 28, 3159, 8251), (1, 11, 3311, 7195), (3, 121, 3665, 5026), (228, 524, 3732, 6754), (51, 1338, 2361, 6259), (1, 3, 4087, 7123), (3, 449, 4235, 7012), (83, 3129, 4491, 5083), (3, 3129, 4491, 5307), (45, 460, 4666, 5057), (3, 203, 1454, 7747), (4, 1338, 2361, 6259), (1338, 1822, 2361, 8158), (1, 1178, 2477, 8326), (1, 3, 1220, 6179), (1, 2523, 2740, 5568), (1, 2523, 2740, 6677), (99, 2523, 2740, 6967), (1, 11, 937, 6342), (1, 843, 3311, 6372), (3, 3129, 4031, 7619), (496, 3545, 4563, 8203), (203, 1075, 1454, 7747), (1, 6, 341, 6318), (3, 7, 610, 8039), (1, 637, 1005, 5900), (1, 4, 125, 5478), (1, 10, 1982, 7478), (3, 49, 3129, 7551), (1, 937, 2948, 5468), (3, 610, 3057, 6278), (1, 1005, 2203, 5710), (1, 1005, 2203, 7836), (4, 955, 1090, 7669), (582, 1805, 2543, 5106), (582, 1805, 2543, 7385), (1, 1005, 1241, 5900), (3, 203, 3642, 5939), (3, 3642, 3715, 8465), (6, 634, 2148, 6652), (6, 471, 634, 8453), (1, 121, 6338, 6522), (1, 3, 6522, 7807), (3, 121, 6522, 8309), (6, 86, 6951, 7142), (278, 458, 5809, 7445), (3, 203, 5917, 8054), (1, 3, 5605, 7123), (1, 3, 7331, 8041), (86, 701, 5805, 8322), (86, 102, 5997, 8322), (1, 777, 5113, 5982), (3, 519, 6475, 6669), (3, 121, 6182, 8446), (4, 51, 2361, 6259), (1, 112, 6132, 8326), (1, 3, 5927, 6255), (1, 3, 5927, 7794), (1, 3, 5587, 6518), (3, 121, 5026, 8292), (3, 4491, 5307, 6429), (3, 4491, 5307, 7640), (1, 1178, 6507, 8326), (1, 2740, 5568, 7361), (1, 4, 5075, 5478), (1, 4, 5151, 5478), (1, 1005, 5710, 7356), (6, 634, 6143, 6652), (634, 2148, 6652, 6697), (3, 6522, 6913, 8309), (3, 6522, 7749, 8309), (1, 3, 6172, 7794), (1, 3, 6518, 7627), (1, 3, 6518, 7918), (4491, 5307, 6429, 6589), (1, 2740, 5391, 7361), (3, 7123, 7749, 8309), (3, 5565, 7123, 8309), (4, 51, 1338, 2361, 6259), (1, 3, 28, 8816), (1, 3, 28, 9000), (4, 51, 175, 9030), (3, 17, 449, 9452), (296, 496, 509, 9876), (1, 3, 572, 9907), (1, 90, 112, 8506), (553, 626, 686, 9318), (1, 86, 1711, 9070), (1, 86, 1711, 9467), (3, 203, 2350, 9429), (3, 121, 2557, 9181), (3, 449, 3159, 9156), (17, 449, 3159, 9395), (21, 489, 3687, 9545), (3, 263, 4235, 9071), (6, 1063, 4877, 8963), (1, 1447, 1953, 9346), (449, 1123, 4235, 9642), (1, 10, 572, 8628), (1, 10, 1982, 9478), (4, 53, 1822, 8765), (634, 1338, 1822, 9963), (129, 203, 2350, 9429), (4, 1822, 3286, 8765), (445, 529, 4483, 8572), (445, 529, 2104, 9007), (129, 203, 1758, 9429), (3, 3159, 3715, 8978), (3, 594, 1568, 9232), (1, 3, 8252, 9000), (4, 1029, 6062, 9664), (3, 121, 6182, 9181), (1, 112, 8326, 8506), (3, 121, 5026, 9591), (1, 1178, 8326, 9070), (2523, 2740, 5568, 8588), (1, 3, 7794, 9085), (1, 3, 6518, 9907), (3, 5026, 8292, 9547), (6, 634, 6143, 9427), (6, 634, 6143, 9521), (1, 3, 8735, 9000), (553, 626, 9318, 9376), (3, 2350, 9162, 9429), (3, 203, 9429, 9591), (3, 3159, 9156, 9560), (1123, 4235, 9348, 9642), (3, 121, 9429, 9591), (6, 634, 9427, 9512), (3, 8681, 8735, 9000), (3, 9162, 9429, 9591), (6, 399, 1063, 4219, 4877), (4, 51, 1338, 2361, 6259)]
    foursList=len(fours)
    fives=[]
    for combo in fours:
        for i in range(8499,10000):
            newCombo=compatible(i,combo,primeList)
            if len(newCombo)==5 and not (newCombo in fours):
                fives.append(newCombo)
                fours.append(newCombo)
                print("FIVE!!!")
                print(newCombo)
            elif len(newCombo)==4 and not (newCombo in fours):
                fours.append(newCombo)
                print("four:",newCombo,len(fours))
        print(fours.index(combo), "out of", len(fours), ":", combo)
        if len(fours)>foursList+500:
            break
    outFile=open("foursFives.txt","w")
    outFile.write(str(fours))
    outFile.write("\n\n")
    outFile.write(str(fives))
    outFile.close()

    for combo in fives:
        print("Fives:")
        for i in combo:
            print("i=",i,"prime number:",primeList[i],end=", ")
        print()
        print("total=",comboTotal(combo,primeList))

def main60_e():
    primeList=primeListFile(10000000,"primes.txt")
    fours=[(8, 14, 575, 724), (3, 7, 519, 745), (4, 626, 686, 767), (1, 11, 18, 777), 
    (8, 131, 285, 822), (1, 6, 86, 826), (1, 6, 86, 852), (6, 399, 541, 886), (3, 203, 519, 891), 
    (51, 175, 282, 952), (1, 11, 777, 1005), (4, 8, 285, 1025), (1, 4, 311, 1029), 
    (275, 424, 586, 1057), (6, 399, 627, 1063), (4, 8, 285, 1080), (1, 4, 311, 1090), 
    (14, 233, 575, 1113), (3, 83, 504, 1185), (6, 86, 826, 1222), (1, 11, 351, 1254), 
    (4, 51, 175, 1338), (1, 86, 311, 1711), (1, 11, 572, 1936), (1, 90, 582, 1953), 
    (1, 99, 572, 1982), (1, 11, 572, 1982), (6, 399, 886, 2104), (4, 285, 1080, 2254), 
    (4, 175, 1338, 2342), (3, 28, 121, 2348), (3, 203, 519, 2350), (11, 18, 777, 2355), 
    (4, 51, 1338, 2361), (3, 83, 504, 2438), (1, 112, 582, 2477), (1, 3, 121, 2557), 
    (4, 1080, 2254, 2594), (8, 497, 675, 2604), (1, 3, 2557, 2719), (1, 99, 1982, 2740), 
    (1, 11, 1982, 3059), (3, 83, 1185, 3129), (6, 399, 2104, 3143), (1, 3, 28, 3159), 
    (3, 17, 449, 3159), (3, 28, 2348, 3159), (1, 11, 572, 3311), (11, 1982, 3059, 3614), 
    (3, 28, 121, 3665), (21, 162, 489, 3687), (228, 408, 524, 3732), (4, 181, 282, 3745), 
    (21, 186, 489, 3877), (51, 1338, 2361, 3943), (203, 519, 891, 4054), (203, 519, 2350, 4054), 
    (28, 121, 3665, 4073), (1, 3, 2719, 4087), (6, 399, 1063, 4219), (3, 263, 449, 4235), 
    (272, 296, 496, 4381), (6, 399, 2104, 4483), (3, 83, 3129, 4491), (21, 278, 496, 4563), 
    (45, 460, 682, 4666), (6, 399, 1063, 4877)]
    foursList=len(fours)
    fives=[]
    for combo in fours:
        i=combo[-1]   
        while i>701:
            newCombo=compatible(i,combo,primeList)
            if len(newCombo)==5:
                fives.append(newCombo)
                print("FIVE!!!")
                print(newCombo)
            elif len(newCombo)==4 and not (newCombo in fours):
                fours.append(newCombo)
                print("four:",newCombo,len(fours))
            i-=1
        print(fours.index(combo), "out of", len(fours), ":", combo)
        if len(fours)>foursList+100:
            break
    outFile=open("foursFives.txt","w")
    outFile.write(str(fours))
    outFile.write("\n\n")
    outFile.write(str(fives))
    outFile.close()

    for combo in fives:
        print("Fives:")
        for i in combo:
            print("i=",i,"prime number:",primeList[i],end=", ")
        print()
        print("total=",comboTotal(combo,primeList))



def main60_d():
    primeList=primeListFile(10000000,"primes.txt")
    fours=[(1, 3, 28, 121), (8, 63, 122, 143), (4, 51, 175, 282), (4, 51, 181, 282), 
    (4, 8, 131, 285), (8, 122, 143, 285), (1, 6, 86, 311), (10, 187, 307, 338), 
    (1, 4, 311, 341), (1, 11, 18, 351), (56, 112, 153, 399), (3, 202, 243, 432), 
    (3, 17, 263, 449), (3, 315, 424, 449), (3, 144, 386, 473), (11, 243, 393, 484), 
    (21, 162, 186, 489), (21, 278, 458, 496), (11, 166, 336, 504), (3, 83, 232, 504), 
    (272, 296, 496, 509), (3, 7, 24, 519), (3, 7, 203, 519), (229, 392, 479, 522), 
    (139, 217, 322, 547), (228, 408, 524, 558), (214, 333, 404, 568), (1, 3, 99, 572), 
    (1, 11, 351, 572), (8, 14, 233, 575), (3, 315, 449, 577), (1, 90, 112, 582), 
    (275, 424, 509, 586), (25, 381, 392, 591), (308, 462, 523, 614), (77, 154, 542, 618), 
    (6, 399, 541, 627), (14, 160, 227, 657), (23, 27, 177, 665), (8, 303, 497, 675), 
    (45, 460, 590, 682), (4, 553, 626, 686), (14, 53, 685, 698), (80, 86, 102, 701)]
    fives=[]
    i=702

    while i<5000:
        toAdd=[]
        for combo in fours:
            newCombo=compatible(i,combo,primeList)
            if len(newCombo)==5:
                fives.append(newCombo)
                print("FIVE!!!")
                print(newCombo)
            elif len(newCombo)==4 and not (newCombo in toAdd):
                toAdd.append(newCombo)
                print("four:",newCombo,len(fours))
        for combo in toAdd:
            fours.append(combo)
        i+=1 
        if i%200==0:
            print("i=", i)

    outFile=open("foursFives.txt","w")
    outFile.write(str(fours))
    outFile.write("\n\n")
    outFile.write(str(fives))
    outFile.close()

    for combo in fives:
        print("Fives:")
        for i in combo:
            print("i=",i,"prime number:",primeList[i],end=", ")
        print()
        print("total=",comboTotal(combo,primeList))


def main60_c():
    primeList=primeListFile(10000000,"primes.txt")
    catCombos=[(1,3)]
    i=4
    fives=[]
    fours=[]
    done=False
    #print(isPrime(1234123478,primeList))
    
    print("total=",comboTotal([5, 691, 750, 867, 1050],primeList))
    while not done:
        toAdd=[]
        fullReplace=[]
        for j in range(len(catCombos)):
            newCombo=compatible(i,catCombos[j],primeList)
            if len(newCombo)==len(catCombos[j])+1:
                catCombos[j]=newCombo
                fullReplace.append(newCombo)
                announce(newCombo,catCombos,fours,fives)
            elif len(newCombo)>1 and not (newCombo in toAdd):
                toAdd.append(newCombo)
        if len(toAdd)==0 and len(fullReplace)==0:
            toAdd.append((i,))
        for combo in toAdd:
            if not (combo in fullReplace):
                announce(newCombo,catCombos,fours,fives)
                catCombos.append(combo)
        i+=1 
        if i>2500 or len(fives)>=5:
            done=True            
    for combo in fives:
        print("Fives:")
        for i in combo:
            print("i=",i,"prime number:",primeList[i],end=", ")
        print()
        print("total=",comboTotal(combo,primeList))
    for combo in fours:
        print("Fours:")
        for i in combo:
            print("i=",i,"prime number:",primeList[i],end=", ")
        print()
        print("total=",comboTotal(combo,primeList))
    outFile=open("foursFives.txt","w")
    outFile.write(str(fours))
    outFile.write("\n\n")
    outFile.write(str(fives))
    outFile.close()

    outFile=open("catCombos.txt","w")
    outFile.write(str(catCombos))

"""
[(1, 3, 28, 121), (8, 63, 122, 143), (4, 51, 175, 282), (4, 51, 181, 282), (4, 8, 131, 285), 
(8, 122, 143, 285), (1, 6, 86, 311), (10, 187, 307, 338), (1, 4, 311, 341), (1, 11, 18, 351), 
(56, 112, 153, 399), (3, 202, 243, 432), (3, 17, 263, 449), (3, 315, 424, 449), (3, 144, 386, 473), 
(11, 243, 393, 484), (21, 162, 186, 489), (21, 278, 458, 496), (11, 166, 336, 504), (3, 83, 232, 504), 
(272, 296, 496, 509), (3, 7, 24, 519), (3, 7, 203, 519), (229, 392, 479, 522), (139, 217, 322, 547), 
(228, 408, 524, 558), (214, 333, 404, 568), (1, 3, 99, 572), (1, 11, 351, 572), (8, 14, 233, 575), 
(3, 315, 449, 577), (1, 90, 112, 582), (275, 424, 509, 586), (25, 381, 392, 591), (308, 462, 523, 614), 
(77, 154, 542, 618), (6, 399, 541, 627), (14, 160, 227, 657), (23, 27, 177, 665), (8, 303, 497, 675), 
(45, 460, 590, 682), (4, 553, 626, 686), (14, 53, 685, 698), (80, 86, 102, 701)]


[(1, 3, 28, 121), (8, 63, 122, 143), (4, 51, 175, 282), (4, 51, 181, 282), (4, 8, 131, 285), 
(8, 122, 143, 285), (1, 6, 86, 311), (10, 187, 307, 338), (1, 4, 311, 341), (1, 11, 18, 351), 
(56, 112, 153, 399), (3, 202, 243, 432), (3, 17, 263, 449), (3, 315, 424, 449), 
(3, 144, 386, 473), (11, 243, 393, 484), (21, 162, 186, 489), (21, 278, 458, 496), 
(11, 166, 336, 504), (3, 83, 232, 504), (272, 296, 496, 509), (3, 7, 24, 519), (3, 7, 203, 519), 
(229, 392, 479, 522), (139, 217, 322, 547), (228, 408, 524, 558), (214, 333, 404, 568), 
(1, 3, 99, 572), (1, 11, 351, 572), (8, 14, 233, 575), (3, 315, 449, 577), (1, 90, 112, 582), 
(275, 424, 509, 586), (25, 381, 392, 591), (308, 462, 523, 614), (77, 154, 542, 618), 
(6, 399, 541, 627), (14, 160, 227, 657), (23, 27, 177, 665), (8, 303, 497, 675), 
(45, 460, 590, 682), (4, 553, 626, 686), (14, 53, 685, 698), (80, 86, 102, 701), 

(8, 14, 575, 724), (3, 7, 519, 745), (4, 626, 686, 767), (1, 11, 18, 777), 
(8, 131, 285, 822), (1, 6, 86, 826), (1, 6, 86, 852), (6, 399, 541, 886), (3, 203, 519, 891), 
(51, 175, 282, 952), (1, 11, 777, 1005), (4, 8, 285, 1025), (1, 4, 311, 1029), 
(275, 424, 586, 1057), (6, 399, 627, 1063), (4, 8, 285, 1080), (1, 4, 311, 1090), 
(14, 233, 575, 1113), (3, 83, 504, 1185), (6, 86, 826, 1222), (1, 11, 351, 1254), 
(4, 51, 175, 1338), (1, 86, 311, 1711), (1, 11, 572, 1936), (1, 90, 582, 1953), 
(1, 99, 572, 1982), (1, 11, 572, 1982), (6, 399, 886, 2104), (4, 285, 1080, 2254), 
(4, 175, 1338, 2342), (3, 28, 121, 2348), (3, 203, 519, 2350), (11, 18, 777, 2355), 
(4, 51, 1338, 2361), (3, 83, 504, 2438), (1, 112, 582, 2477), (1, 3, 121, 2557), 
(4, 1080, 2254, 2594), (8, 497, 675, 2604), (1, 3, 2557, 2719), (1, 99, 1982, 2740), 
(1, 11, 1982, 3059), (3, 83, 1185, 3129), (6, 399, 2104, 3143), (1, 3, 28, 3159), 
(3, 17, 449, 3159), (3, 28, 2348, 3159), (1, 11, 572, 3311), (11, 1982, 3059, 3614), 
(3, 28, 121, 3665), (21, 162, 489, 3687), (228, 408, 524, 3732), (4, 181, 282, 3745), 
(21, 186, 489, 3877), (51, 1338, 2361, 3943), (203, 519, 891, 4054), (203, 519, 2350, 4054), 
(28, 121, 3665, 4073), (1, 3, 2719, 4087), (6, 399, 1063, 4219), (3, 263, 449, 4235), 
(272, 296, 496, 4381), (6, 399, 2104, 4483), (3, 83, 3129, 4491), (21, 278, 496, 4563), 
(45, 460, 682, 4666), (6, 399, 1063, 4877)]

[(6, 399, 1063, 4219, 4877)]
"""

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

main60_c()





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
