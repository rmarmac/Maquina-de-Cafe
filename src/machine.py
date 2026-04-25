from .user import Users
from .drinks import *

class Operational:
    def __init__(self, keys_admins:dict):
        self.users = Users(keys_admins)
        self.ingredients = []
        self.drinks = []

    @staticmethod
    def checar_permissao(nvl_acesso_necess:int):
            def decorador(funcao_original):
                def wrapper(instancia,user,password,*args,**kwargs):
                    if instancia.users.validate_user(user, password) == True:
                        if instancia.users.get_nvl_acesso(user) == nvl_acesso_necess:
                            funcao_original(instancia,user,password,*args,**kwargs)
                        else:
                            print("Nivel de acesso incompatível!")
                    else:
                        print("Acesso Negado!")
                return wrapper
            return decorador

    def is_available():
        pass

    def choose_drink():
        pass

    def pay():
        pass

    def buy_drink():
        pass

    # Gets ----------------------------------------------------------------------

    @checar_permissao(nvl_acesso_necess=1)
    def get_total_sales(self, user, password):
        pass
    @checar_permissao(nvl_acesso_necess=1)
    def get_can_sales(self, user, password):
        pass
    @checar_permissao(nvl_acesso_necess=1)
    def get_dosed_sales(self, user, password):
        pass
    @checar_permissao(nvl_acesso_necess=1)
    def get_balance(self, user, password):
        pass

    # Sets ----------------------------------------------------------------------

    @checar_permissao(nvl_acesso_necess=1)
    def set_place(self, user, password):
        pass

    @checar_permissao(nvl_acesso_necess=0)
    def update_stock(self, user, password):
        opcao = input("Informe o que deve ser atualizado (ingrediente/lata): ")
        while(opcao != "ingrediente" and opcao != "lata"):
            opcao = input("Selecione uma opcao valida (ingrediente/lata): ")
        if opcao == "lata":
            print("Informe a marca, o nome e quanto deverá ser acrescido/descrescido: ")
            marca = input("Marca: ")
            nome = input("Nome: ")
            delta_qtd = int(input("Acrescimo/Decrescimo: "))
            atualizado = False
            for drink in self.drinks:
                if drink.name == nome and drink.marca == marca:
                    print(f"Bebida {nome} da marca {marca} atualizada, quantidade: {drink.quantity} -> {drink.quantity+delta_qtd}")
                    drink.quantity += delta_qtd
                    atualizado = True
            if not atualizado:
                if delta_qtd > 0:
                    self.drinks.append(CannedDrink(delta_qtd, marca, nome, PRECO_LATA))
        else:
            print("Informe o ingrediente sendo reposto seguido pela modificacao na quantidade: ")
            ingrediente_reposto = input("Ingrediente: ")
            delta_qtd = int(input("Acrescimo/Decrescimo: "))
            atualizado = False
            for ingrediente in self.ingredients:
                if ingrediente.name == ingrediente_reposto:
                    ingrediente.quantity += delta_qtd
                    print(f"Ingrediente {ingrediente_reposto} atualizado, quantidade: {ingrediente.quantity} -> {ingrediente.quantity+delta_qtd}")
                    atualizado = True
            if not atualizado:
                if delta_qtd > 0:
                    self.ingredients.append(Ingredient(ingrediente_reposto, delta_qtd))





class Machine:
    def __init__(self, id_machine:int, place:str, keys_admins:dict):
        self.id_machine = id_machine
        self.place = place
        self.operational = Operational(keys_admins)

    # Gets --------------------------------------------------------------------------------------

    def get_place(self):
        return self.place
    
    def get_id(self):
        return self.id_machine

    # Operacoes  -------------------------------------------------------------------------------

    def initial_screen():
        pass

    def buy_drink():
        pass