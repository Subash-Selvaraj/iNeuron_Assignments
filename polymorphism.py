#polymorphism
#one function and multiple behaviour
#one person and multiple relationships with different different peoples(brother,son,uncle..etc
class ineuron:
    def students(self):
        print("print a students details")

class class_type:
    def class_for_students(self):
        print("print the class type")
#externa method
def ineuron_external(a):
    a.students()

i = ineuron()
j = class_type()
ineuron_external(i)

#example of simle understanding of polymarpshism
def test(a,b):
    return a+b
print(test(2,3)) #addition operation
print(test("subash","S")) #concat operation
