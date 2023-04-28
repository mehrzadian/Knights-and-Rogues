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
        
