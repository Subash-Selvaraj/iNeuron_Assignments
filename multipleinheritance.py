class bank:
    def transaction(self):
        print("TOTAL transaction Value")
    def account_openeing(self):
        print("This will shoe you your accounct open status")
    def deposite(self):
        print("this will show you your deposited amount")
    def test(self):
        print("this is the test method from bank class")

class HDFC_Bank():
    def hdfc_to_icic(self):
        print('this will show you all the transaction happened to icici through hdfc')
    def test(self):
        print("this is the test method from the hdfc bank")

class ineuron_bank():
    def account_status_icici(self):
        print("print the account status in ineuron ICICI")

class icici(bank,HDFC_Bank,ineuron_bank):#inherit the all classes inthe one class it is called tha multiple inheritance in python
    def total(self):
        print("this is the final class which is inherited all the class")
i = icici()
i.deposite()
i.transaction()
i.hdfc_to_icic()
i.test()
i.account_status_icici()
'''we have test method in two class.so inthis point in python the first declared method
will be called in the inheritance functionality.so in the icici class we have called the bank class first 
so the bank class test method will be called'''
i.total()
