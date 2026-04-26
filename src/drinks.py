from dataclasses import dataclass
from abc import ABC

PRECO_LATA : int = 5
PRECO_DOSADA : int = 10

@dataclass
class Ingredient:
    def __init__(self, name:str, quantity:int):
        self.name = name
        self.quantity = quantity

@dataclass
class Drink(ABC):
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price

@dataclass
class CannedDrink(Drink):
    def __init__(self, quantity:int, marca:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quantity = quantity
        self.marca = marca

@dataclass
class DosedDrink(Drink):
    def __init__(self, ingredients_needed:list[Ingredient], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ingredients_needed = ingredients_needed