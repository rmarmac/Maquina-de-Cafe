class Ingredient:
    def __init__(self, name:str, quantity:int):
        self.name = name
        self.quantity = quantity

class Drink():
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price

class CannedDrink(Drink):
    def __init__(self, quantity:int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quantity = quantity

class DosedDrink(Drink):
    def __init__(self, available_doses:list, ingredients_needed:list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.available_doses = available_doses
        self.ingredients_needed = ingredients_needed