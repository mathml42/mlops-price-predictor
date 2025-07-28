from abc import ABC, abstractmethod

class DinnerExperience(ABC):

    def serve_dinner(self):
        self.serve_appetizer()
        self.serve_main_course()
        self.serve_dessert()
        self.serve_beverage()

    @abstractmethod
    def serve_appetizer(self):
        pass

    @abstractmethod
    def serve_main_course(self):
        pass
    
    @abstractmethod
    def serve_dessert(self):
        pass
    
    @abstractmethod
    def serve_beverage(self):
        pass

# Step 2: Create concrete classes that implement the template steps
class IndianCuisine(DinnerExperience):
    def serve_appetizer(self):
        return print("Serve Kebab.")
    
    def serve_main_course(self):
        return print("Serve Paneer Butter Masala & Naan.")
    
    def serve_beverage(self):
        return print("Serve Mango Lassi.")
    
    def serve_dessert(self):
        return print("Serve Rasmalai.")

# Similarly you can try different cuisine.
class ItalianDinner(DinnerExperience):
    def serve_appetizer(self):
        print("Serving bruschetta as appetizer.")

    def serve_main_course(self):
        print("Serving pasta as the main course.")

    def serve_dessert(self):
        print("Serving tiramisu as dessert.")

    def serve_beverage(self):
        print("Serving wine as the beverage.")


class ChineseDinner(DinnerExperience):
    def serve_appetizer(self):
        print("Serving spring rolls as appetizer.")

    def serve_main_course(self):
        print("Serving stir-fried noodles as the main course.")

    def serve_dessert(self):
        print("Serving fortune cookies as dessert.")

    def serve_beverage(self):
        print("Serving tea as the beverage.")

if __name__=="__main__":
    dinner = ChineseDinner()
    dinner.serve_dinner()