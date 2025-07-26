from abc import ABC, abstractmethod

# 1. Define the strategy interface
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# 2. Define the concrete strategies
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} rupees using credit card."

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} rupees using Paypal."
    
class UPIPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} rupees using UPI."
    
# 3. Implement the context
class ShoppingCart:
    def __init__(self, method: PaymentMethod):
        self.method = method
    def checkout(self,amount):
        return self.method.pay(amount)
    
# 4. Use the strategy in the context
if __name__=="__main__":
    cart = ShoppingCart(CreditCardPayment())
    print(cart.checkout(100))

    cart = ShoppingCart(PayPalPayment())
    print(cart.checkout(100))

    cart = ShoppingCart(UPIPayment())
    print(cart.checkout(100))