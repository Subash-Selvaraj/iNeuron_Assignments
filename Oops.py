#Inheritence
class car: #parent class
    def __init__(self,body,engine,tyer):
        self.body = body
        self.engine = engine
        self.tyer = tyer
    def milage(self):
        print("Milage of this car")
c=car('solid','b6','2015')
print(c)

class tata(car): #inherit #child class
    pass

t = tata('liquid','b5','ceat') #provide the parameters which we have declared in the parent class then only we will ingerit everything from tha parent class

t.milage() #call the oanother funtion which is inside the parent class
print(t)





