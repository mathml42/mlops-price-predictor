from abc import ABC, abstractmethod

# 1. Defing a abstract class
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

# 2. Implementing the concrete products
class Espresso(Coffee):
    def prepare(self):
        return "Preparing a rich and strong Espresso."

class Latte(Coffee):
    def prepare(self):
        return "Preparing a smooth and creamy latte"
    
class Cappucino(Coffee):
    def prepare(self):
        return "Preparing a frothy cappucino"
    
# 3. Implementing the coffee machine 
class CoffeeMachine:
    def make_coffee(self, coffee_type):
        if coffee_type == "espresso":
            return Espresso().prepare()
        elif coffee_type == "latte":
            return Latte().prepare()
        elif coffee_type == "cappucino":
            return Cappucino().prepare()
        else:
            return "This coffee is not available"

# 4. Preparing coffee using our factory
if __name__ == "__main__":
    coffee_maker = CoffeeMachine()
    # to prepare Espresso
    coffee = coffee_maker.make_coffee('espresso')
    print(coffee)
    # to prepare Latte
    coffee = coffee_maker.make_coffee("latte")
    print(coffee)
    # to prepare Cappucino
    coffee = coffee_maker.make_coffee("cappucino")
    print(coffee)