from product import Pizza

class BuilderPizza:
    """Interface Builder for building pizzas.
    """
    def build_dough(self):
        """Builds the pizza dough.
        """
        pass

    def build_cheese(self):
        """Adds cheese to pizza.
        """
        pass

    def build_sauce(self):
        """Adds sauce to pizza.
        """
        pass

    def build_igredients(self):
        """Add the other ingredients specific to each pizza.
        """
        pass

    def get_pizza(self):
        """Returns the pizza that was built.
        """
        pass

class BuilderClassicPizza(BuilderPizza):
    """Responsible for building a classic pizza, inheriting and implementing 
    the methods of the BuilderPizza class to build the pizza flavor.
    """
    def __init__(self):
        """A new pizza is created and the reference is stored in the instance variable.
        """
        self.pizza = Pizza()

    def build_dough(self):
        """Build the pizza dough
        """
        self.pizza.add_ingredient("Classic Pizza Dough")

    def build_cheese(self):
        """Add cheese to pizza.
        """
        self.pizza.add_ingredient("Cheese")

    def build_sauce(self):
        """Add sauce to pizza.
        """
        self.pizza.add_ingredient("Special Sauce")

    def build_igredients(self):
        """Add the specific pizza ingredient.
        """
        self.pizza.add_ingredient("Peperonni")

    def get_pizza(self):
        """Gets the pizza built.

         Returns:
             Pizza: The constructed Pizza object.
        """
        return self.pizza
    
    
class BuilderChickenPizza(BuilderPizza):
    """Responsible for building a chicken pizza, inheriting and implementing 
    the methods of the BuilderPizza class to build the pizza flavor.
    """
    def __init__(self):
        """A new pizza is created and the reference is stored in the instance variable.
        """
        self.pizza = Pizza()

    def build_dough(self):
        """Build the pizza dough
        """
        self.pizza.add_ingredient("Thin Pizza Dough")

    def build_cheese(self):
        """Add cheese to pizza
        """
        self.pizza.add_ingredient("Cheese")

    def build_sauce(self):
        """Add sauce to pizza.
        """
        self.pizza.add_ingredient("Special Sauce")

    def build_igredients(self):
        """Add the specific pizza ingredient.
        """
        self.pizza.add_ingredient("Shredded Chicken and Corn")

    def get_pizza(self):
        """Gets the pizza built.

         Returns:
             Pizza: The constructed Pizza object.
        """
        return self.pizza
    

class BuilderMeatPizza(BuilderPizza):
    """Responsible for building a meat pizza, inheriting and implementing 
    the methods of the BuilderPizza class to build the pizza flavor.
    """
    def __init__(self):
        """A new pizza is created and the reference is stored in the instance variable.
        """
        self.pizza = Pizza()

    def build_dough(self):
        """Build the pizza dough.
        """
        self.pizza.add_ingredient("Thin Pizza Dough")

    def build_cheese(self):
        """Add cheese to pizza
        """
        self.pizza.add_ingredient("Cheese")

    def build_sauce(self):
        """Add sauce to pizza.
        """
        self.pizza.add_ingredient("Special Sauce")

    def build_igredients(self):
        """Add the specific pizza ingredient.
        """
        self.pizza.add_ingredient("Shredded Beef")

    def get_pizza(self):
        """Gets the pizza built.

         Returns:
             Pizza: The constructed Pizza object.
        """
        return self.pizza