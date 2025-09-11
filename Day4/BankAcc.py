class Bank:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount:int):
        self.amount=amount
        self.__balance+=self.amount
        print(f"Amount is successfully debited into account")
    def withdraw(self,amount:int):
        self.amount=amount
        if(self.__balance<self.amount):
            print("Insufficient Funds")
        else:
            self.__balance-=self.amount
            print("Amount is successfully withdrawed from bank")
    def get_balance(self):
        return f"Your Bank Balance is {self.__balance}"
b1=Bank()
b1.deposit(5000)
print(f"{b1.get_balance()}")
b1.withdraw(2000)
print(f"{b1.get_balance()}")