class ineuron():
    def student(self):
        print("print the details of all the students")
    def acheiver_lists(self):
        print('print the list of all the achiver')
    def hall_of_frame(self):
        print("print everyone from hall of frame")

class ineuron_vision(ineuron): #inherited
 #override the functions or method
    def student(self): #overriding the method in the child class
        print("these are the filters student lists")

iv = ineuron_vision()
iv.student()