from builders import BuilderClassicPizza, BuilderMeatPizza, BuilderChickenPizza

class Restaurant:
    """The class receives a specific Builder object as a parameter in its constructor. 
    This Builder object is responsible for building a specific type of pizza, with its also 
    specific ingredients.
    """
    def __init__(self, builder):
        """Initializes the restaurant with a specific builder.

        Args:
            builder (BuilderPizza): The builder (Builder) that will be used to build the pizza.

        """
        self.builder = builder

    def build_pizza(self):
        """Build the pizza using the provided Builder.
        """
        self.builder.build_dough()
        self.builder.build_cheese()
        self.builder.build_sauce()
        self.builder.build_igredients()

    def get_pizza(self):
        """Returns the constructed pizza.

        Returns:
            Pizza: The pizza built by the provided Builder.
        """
        return self.builder.get_pizza()