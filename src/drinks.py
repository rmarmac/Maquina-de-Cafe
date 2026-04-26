PRECO_LATA = 5
PRECO_DOSADA = 10

class Ingredient:
    def __init__(self, name:str, quantity:int):
        self.name = name
        self.quantity = quantity

class Drink():
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price

class CannedDrink(Drink):
    def __init__(self, quantity:int, marca:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quantity = quantity
        self.marca = marca

class DosedDrink(Drink):
    def __init__(self, ingredients_needed:list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ingredients_needed = ingredients_needed