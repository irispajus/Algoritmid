# Koodis on lineaarse otsingu algoritm ning ajalise keerukuse mõõtmiseks 
# vajalik programm, mis on hetkel välja kommenteeritud. 

#import time 
def lineaarotsing (list, otsitav):

    for i in range (len(list)):
        if list [i] == otsitav:
            return i

list = [1,2,5,3,7,11,6,9,4,8,12,13,15,16,17,18,19,20,21]
otsitav = 16

#start = time.perf_counter()

tulemus = lineaarotsing(list,otsitav)

#lopp = time.perf_counter()
#ajakulu = (lopp - start) * 1000

print (tulemus)
#print(ajakulu) 
