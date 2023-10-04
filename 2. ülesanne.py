import time

class LIFO:
    def __init__(self):
        self.items = [] #alustamise samm 
        
    def isEmpty(self):
        return self.items == [] #kontrollib kas stack on tühi või ei
    
    def push (self, item):
        self.items.append(item) #lisab andmetüki enda stackki
        
    def pop (self):
        return self.items.pop() #võtab andmetüki oma stackist välja
    
    def size (self):
        return len(self.items) #vaatab stacki suurust
    
    def printLIFO(self):
        for item in self.items:
            print (item,", ", end = '')
            
MinuStack = LIFO() #kasutab LIFO andmeid ja teeb uue andmestruktuuri

#siin defineerin koodi katsetamiseks testandmed, mida stackki lisada, eemaldada
MinuStack.push(5)
MinuStack.push(9)
MinuStack.push(3)

print(MinuStack.isEmpty()) #annab teada kui stack peaks tühi olema

MinuStack.printLIFO() #prindib andmed

MinuData = MinuStack.pop() #võtab viimase andmetüki stackist välja
print("\n", MinuData) #prindib viimase last-in-first-out andmetüki

start = time.time()
for _ in range(1000000):  
    MinuStack.push(1)
push = time.time() - start


start = time.time()
for _ in range(1000000):  
    MinuStack.pop()
pop = time.time() - start

print(f"väärtuse lisamiseks kulunud aeg: {push} sekundit")
print(f"väärtuse väljavõtmiseks kulunud aeg: {pop} sekundit")

#toiming võiks olla 80% parem 
    
    