#multi level or multilable inheritance
class bank:
    def transaction(self):
        print("TOTAL transaction Value")
    def account_openeing(self):
        print("This will shoe you your accounct open status")
    def deposite(self):
        print("this will show you your deposited amount")

class HDFC_Bank(bank):#inherted the bank class into the HDFC_bank class
    def hdfc_to_icic(self):
        print('this will show you all the transaction happened to icici through hdfc')

class icici(HDFC_Bank):
    pass

i = icici() #create an object for the class to get the methods those are available inside the classes

 #by using the object to call the methods from the another classes and this has been called multi lable inheritance
i.transaction()
i.account_openeing()
i.deposite()
i.hdfc_to_icic()


