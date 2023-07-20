from product import Pizza
from builders import BuilderPizza, BuilderClassicPizza, BuilderChickenPizza, BuilderMeatPizza
from director import Restaurant

if __name__ == "__main__":
    """Example of using the Builder pattern to create pizzas with different flavors.

    1. Create a classic pizza
    2. Create a meat pizza
    3. Create a chicken pizza

    The steps for building the pizzas are encapsulated by the Builders (BuilderClassicPizza, BuilderMeatPizza 
    and BuilderChickenPizza), and the Director (Restaurant)
    directs the construction process for each type of pizza.

    At the end, we have the list of ingredients that are part of each pizza.
    """
    print("CLASSIC PIZZA")
    builder_classic_pizza = BuilderClassicPizza()
    restaurant = Restaurant(builder_classic_pizza)
    restaurant.build_pizza()
    classic_pizza = restaurant.get_pizza()
    classic_pizza.list_ingredients() 

    print("\nMEAT PIZZA")
    builder_meat_pizza = BuilderMeatPizza()
    restaurant = Restaurant(builder_meat_pizza)
    restaurant.build_pizza()
    meat_pizza = restaurant.get_pizza()
    meat_pizza.list_ingredients() 

    print("\nCHICKEN PIZZA")
    builder_chicken_pizza = BuilderChickenPizza()
    restaurant = Restaurant(builder_chicken_pizza)
    restaurant.build_pizza()
    chicken_pizza = restaurant.get_pizza()
    chicken_pizza.list_ingredients() 