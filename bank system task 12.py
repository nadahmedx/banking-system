import time
database = {}


class Bank:

    def _init_(self, name, balance):

        self.name = name
        self.balance = balance
        database.update({name: balance})

    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        if amount > 0:
            self.balance += amount
            print("Successful Transaction.\nNew Balance:"+str(self.balance))
            database[self.name] = self.balance
        else:
            print('Unsuccessful Transaction.\nTry again')

    def withdraw(self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print("Successful Transaction.\nNew Balance:"+str(self.balance))
            database[self.name] = self.balance
        else:
            print('Unsuccessful Transaction\nTry again')

    def transfer(self):
        receiver = input("Enter the name of receiver:")
        if receiver in database.keys() and receiver != self.name:
            amount = int(input("Enter the amount:"))
            if amount <= self.balance:
                self.balance -= amount
                database[self.name] = self.balance
                print(
                    f"Successful Transaction\n{str(amount)} transferred to {receiver}\n Your New Balance:{self.balance}")
            else:
                print("Unsuccessful Transaction.Try again")
        else:
            print("TRY AGAIN")