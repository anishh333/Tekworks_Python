from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} in Cash"
    
class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Card"
    
class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} via UPI"

payments = [CashPayment(), CardPayment(), UPIPayment()]

for p in payments:
    print(p.pay(1000))
