#Abstraction
#where we have hiding the data behind something that is called data abstractipon
#when the use is hiding the __students variable behind the class that is called the abstraction.why we are say hiding means we will not get the variable by directly on that case we have call the class first and the call the variable so this is called the data hiding or abstraction

class ineuron:
    __students = "data science" #private variable because the variable has been declared with __
    def students(self):
        print("print the class students",ineuron.__students) #while calling the private variable we have to call the class first and import the variable

i = ineuron()
i.students()
print(i._ineuron__students) #private variable  calling

