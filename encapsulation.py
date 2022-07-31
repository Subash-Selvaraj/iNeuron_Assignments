class ineuron:
    def __init__(self):
        self.Students1 = "data science"
    def students(self):
        print(self.Students1)

i = ineuron()
i.students()
i.Students1= 'Data analytics'#override the public variable value in runtime#but in private variable we can't cvhange the value in runt time for that we can override in another method for the same private variable
i.students()

class ineuron1:
    def __init__(self):
        self.__Students1 = "data science"
    def students(self):
        print(self.__Students1)

    #create a another class to overiwrte the private variable value
    def change_private(self):
        self.__Students1='Big data'

i1 = ineuron1()
i1.students()
i1.Students1= 'Big data' #it will not overide becaus its is private variable and we are not able to change in run time
i1.students() #it will not change tha value of the variable
i1.change_private() #it will change the private variable value
i1.students() #here the data will changed and give the chaged data

