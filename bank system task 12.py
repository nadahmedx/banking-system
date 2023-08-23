database={}

class Bank:

    def __init__(self,name,age,balance):
        self.name=name
        self.age=age
        self.balance=balance

        if age<21:
            print("You can't have a bank account")

        else:
            print("sucessfully registred") 

    def  bank_account(name,balance):
        database.update({name:balance})  
        return database
    
    def deposit(balance,amount):

        if amount>0:
          balance=balance+amount
          print("Successful Transaction\nNew balance:"+str(balance))

        else:
            print("unsuccessful transaction")

    def withdraw(balance,amount): 
        if amount>balance or amount<0:
            print("Unsuccessful Transaction")  

        else:
            balance=balance-amount
            print("successful transaction\nNew balance:"+str(balance))         

    
    
d=Bank("nada",16,10000)
print(Bank.bank_account("nada",10000))
s=Bank.deposit(10000,10000)
t=Bank.withdraw(20000,10000)

