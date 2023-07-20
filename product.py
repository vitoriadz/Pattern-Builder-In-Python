class Pizza:
    """The class represents our final product, a pizza.
    """
    def __init__(self):
        """The builder initializes the ingredients attribute as an 
        empty list, which will be used to store the pizza ingredients.
        """
        self.ingredients = []

    def add_ingredient(self, ingredient):
        """Adds an ingredient to the pizza ingredients list.

        Args:
            ingredient (str): The ingredient to be added.
        """
        self.ingredients.append(ingredient)

    def list_ingredients(self):
        """Displays the pizza ingredients.
        """
        print(f"Pizza ingredients: {', '.join(self.ingredients)}")