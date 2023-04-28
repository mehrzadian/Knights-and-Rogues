import random
class Person:
    '''person with attribute of honesty and id, which can evalute others'''
    def __init__(self,honesty,id):
        self.honesty = honesty
        self.id = id
    def ishonest(self, p2):
        '''if the person is honest will tell the truth about the other one, otherwise 
        he will tell sth random'''
        if self.honesty==True:
            return p2.honesty
        else :
            r = random.randint(0,1)
            if r==0:
                return False
            return True
    def __str__(self):
        return str(self.honesty)+"-"+str(self.id)
        
import random
     
n = int(input())
def seq(n):
    '''create the sequence of people with respect to n 
    in which  honests are more'''
    ls=[]
    zeros=0
    for i in range(n):
        r = random.randint(0,1)
        if r==0:
            zeros+=1
            if n%2==1 and zeros<= n//2:
                p=Person(honesty=False,id=i)
            elif n%2==0 and zeros< n//2:
                p=Person(honesty=False,id=i)
            else:
                p=Person(honesty=True,id=i)
        else:
            p=Person(True,id=i)
        ls.append(p)
    return ls

ls=seq(n)
for i in range(n):
    print(ls[i])

def find_honest(seq):
    ls=[]
    for i in range(0,len(seq)//2,2):
        p1 = seq[i]
        p2 = seq[i+1]
        if p1.ishonest(p2) and p2.ishonest(p1):
            ls.append(p1)
    if len(ls)==0:
        return seq[-1]
    return find_honest(ls)
honest = find_honest(ls)
print("\n\n", honest, "\n\n")