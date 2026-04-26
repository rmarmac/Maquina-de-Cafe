from typing import Callable
from unittest import case

from .user import Users
from .drinks import *
import os

#from src import user


class Operational:
    def __init__(self, keys_admins: dict[str, list[str, int]], place: str):
        self.users = Users(keys_admins)
        self.ingredients : list[Ingredient] = []
        self.drinks : list = []
        self.place : str = place
        self.n_dosadas_vendidas : int = 0
        self.n_latas_vendidas : int = 0

    @staticmethod
    def checar_permissao(nvl_acesso_necess: int) -> Callable:
        def decorador(funcao_original : Callable) -> Callable:
            def wrapper(instancia, user, password, *args, **kwargs):
                if instancia.users.validate_user(user, password) == True:
                    if instancia.users.get_nvl_acesso(user) == nvl_acesso_necess:
                        return funcao_original(instancia, user, password, *args, **kwargs)
                    else:
                        print("Nivel de acesso incompatível!")
                else:
                    print("Acesso Negado!")

            return wrapper

        return decorador

    def pay(self, preco : int) -> bool:
        print("-----------------------------------------------------\n")
        forma_pagamento : str = input(
            f"Preco total ficou em R${preco},00.\nEscolha uma forma de pagamento (pix/credito/debito): ").lower()
        if forma_pagamento == "pix":
            resp : str = input(
                "Aqui esta a chave pix: d81d827dd918d1d9g839hjcjc8189ujv849vbb9nnxsdo812798v6sa5\nJa pagou(s/n)? ")
            if resp == 's':
                print("Obrigado! Aproveite sua bebida.")
                return True
            else:
                print("Pagamento Negado!")
                return False
        elif forma_pagamento == "debito":
            print("Insira seu cartao (ok)")
            input("Insira sua senha:")
            print("Obrigado! Aproveite sua bebida.")
            return True
        else:
            print("Insira seu cartao (ok)")
            qtd_vezes : int = int(input("Quantas vezes deseja parcelar? "))
            if qtd_vezes > 0:
                input("Insira sua senha:")
                print("Obrigado! Aproveite sua bebida.")
                return True
            else:
                print("Erro no pagamento.")
                return False

    def buy_drink(self, tipo_bebida : str):

        if tipo_bebida == "lata":
            canned_drinks : list[CannedDrink] = [x for x in self.drinks if type(x) == CannedDrink]
            if len(canned_drinks) == 0:
                print("Nao temos bebidas em lata no momento...")
                return
            print("Qual das seguintes bebidas deseja comprar?\n")
            print("===============================================")
            for bebida in [x for x in self.drinks if type(x) == CannedDrink]:
                print(f"{bebida.name} - {bebida.marca}")
            print("===============================================")
            nome : str = input("Bebida: ")
            marca : str = input("Marca: ")
            quantidade : int = int(input("Quantidade: "))
            existe : bool = False
            for bebida in canned_drinks:
                if bebida.name.upper() == nome.upper() and bebida.marca.upper() == marca.upper() and quantidade > 0:
                    existe = True
                    if self.pay(min(bebida.quantity, quantidade) * PRECO_LATA):
                        print(f"Aqui esta {min(bebida.quantity, quantidade)} unidade(s) de {nome}/{marca}, Aproveite!")
                        self.n_latas_vendidas += min(bebida.quantity, quantidade)
                        bebida.quantity -= min(bebida.quantity, quantidade)
                    break
            if not existe:
                print("Bebida nao existente.\n")
        else:
            dosed_drinks : list[DosedDrink] = [x for x in self.drinks if type(x) == DosedDrink]
            if len(dosed_drinks) == 0:
                print("Nao temos bebidas dosadas no momento...")
                return
            print("Qual das seguintes bebidas deseja comprar?\n")
            print("===============================================")
            for bebida in dosed_drinks:
                print(bebida.name)
            print("===============================================")
            nome : str = input("Bebida: ")
            dose : int = int(input("Selecione a dose da bebida:\n\n1 - 30%\n2 - 50%\n3 - 70%\n4-100%\n\n "))
            existe = False
            for bebida in dosed_drinks:
                if bebida.name.upper() == nome.upper():
                    existe = True
                    possui_ingredientes_necessarios : bool = True
                    for ingrediente_necessario in bebida.ingredients_needed:
                        suficiente = False
                        for ingrediente_existente in self.ingredients:
                            if ingrediente_existente.name == ingrediente_necessario.name and ingrediente_existente.quantity >= ingrediente_necessario.quantity:
                                suficiente = True
                                break
                        possui_ingredientes_necessarios = possui_ingredientes_necessarios * suficiente

                    if not possui_ingredientes_necessarios:
                        print("Sentimos muito, nao ha ingredientes suficientes para sua compra.\n")
                    else:
                        if self.pay(PRECO_DOSADA):
                            self.n_dosadas_vendidas += 1
                            print(f"Aproveite sua bebida {nome}, dose de {dose}!")
                            for ingrediente_necessario in bebida.ingredients_needed:
                                for ingrediente_existente in self.ingredients:
                                    if ingrediente_existente.name == ingrediente_necessario.name:
                                        ingrediente_existente.quantity -= ingrediente_necessario.quantity
                    break
            if not existe:
                print("Bebida nao existente.\n")

    # Gets ----------------------------------------------------------------------

    @checar_permissao(nvl_acesso_necess=1)
    def get_total_sales(self, user, password):
        return self.n_dosadas_vendidas * PRECO_DOSADA + self.n_latas_vendidas * PRECO_LATA

    @checar_permissao(nvl_acesso_necess=1)
    def get_can_sales(self, user, password):
        return self.n_latas_vendidas * PRECO_LATA

    @checar_permissao(nvl_acesso_necess=1)
    def get_dosed_sales(self, user, password):
        return self.n_dosadas_vendidas * PRECO_DOSADA

    @checar_permissao(nvl_acesso_necess=1)
    def get_balance(self, user, password):
        return self.n_dosadas_vendidas + self.n_latas_vendidas

    def get_place(self):
        return self.place

    # Sets ----------------------------------------------------------------------

    @checar_permissao(nvl_acesso_necess=1)
    def cadastrar_usuario(self, user, password, new_usr, new_password, new_nvl_acesso):
        self.users.cadastrar_user(user, password, new_usr, new_password, new_nvl_acesso)

    @checar_permissao(nvl_acesso_necess=1)
    def set_place(self, user, password):
        self.place = input("Digite qual o novo lugar: ")

    @checar_permissao(nvl_acesso_necess=0)
    def update_stock(self, user, password):
        opcao : str = input("Informe o que deve ser atualizado (ingrediente/lata): ").lower()
        while opcao != "ingrediente" and opcao != "lata":
            opcao = input("Selecione uma opcao valida (ingrediente/lata): ")
        if opcao == "lata":
            print("Informe a marca, o nome e quanto deverá ser acrescido/descrescido: ")
            nome = input("Nome: ")
            marca = input("Marca: ")
            delta_qtd = int(input("Acrescimo/Decrescimo: "))
            atualizado = False
            for drink in self.drinks:
                if drink.name == nome and drink.marca == marca:
                    print(
                        f"Bebida {nome} da marca {marca} atualizada, quantidade: {drink.quantity} -> {drink.quantity + delta_qtd}\n")
                    drink.quantity += delta_qtd
                    atualizado = True
            if not atualizado:
                if delta_qtd > 0:
                    self.drinks.append(CannedDrink(delta_qtd, marca, nome, PRECO_LATA))
                    print("Bebida em lata adicionada com sucesso!\n")
        else:
            print("Informe o ingrediente sendo reposto seguido pela modificacao na quantidade: ")
            ingrediente_reposto = input("Ingrediente: ").lower()
            delta_qtd = int(input("Acrescimo/Decrescimo: "))
            atualizado = False
            for ingrediente in self.ingredients:
                if ingrediente.name == ingrediente_reposto:
                    ingrediente.quantity += delta_qtd
                    print(
                        f"Ingrediente {ingrediente_reposto} atualizado, quantidade: {ingrediente.quantity} -> {ingrediente.quantity + delta_qtd}\n")
                    atualizado = True
            if not atualizado:
                if delta_qtd > 0:
                    self.ingredients.append(Ingredient(ingrediente_reposto, delta_qtd))
                    print("Ingrediente adicionado com sucesso!\n")

    @checar_permissao(nvl_acesso_necess=0)
    def registrar_bebida_dosada(self, user, password):
        nome = input("Informe o nome da bebida: ")
        ingredientes_necessarios = input(
            "Informe os ingredientes necessarios, separados por virgula: ").lower().replace(' ', '').split(',')
        existe = False
        for drink in self.drinks:
            if drink.name == nome:
                drink.ingredients_needed = []
                for nome_ingrediente in ingredientes_necessarios:
                    qtde_necessaria = int(input(f"Informe a quantidade necessaria de {nome_ingrediente} "))
                    drink.ingredients_needed.append(Ingredient(nome_ingrediente, qtde_necessaria))
                print(f"Drink {nome} teve seus ingredientes atualizados!\n")
                existe = True
                break
        if not existe:
            ingredientes = []
            for nome_ingrediente in ingredientes_necessarios:
                qtde_necessaria = int(input(f"Informe a quantidade necessaria de {nome_ingrediente} "))
                ingredientes.append(Ingredient(nome_ingrediente, qtde_necessaria))
            self.drinks.append(DosedDrink(ingredientes, nome, PRECO_DOSADA))
            print("Bebida registrada com sucesso!\n")

class Machine:
    def __init__(self, id_machine: int, place: str, keys_admins: dict[str, list[str, int]]):
        self.id_machine = id_machine
        self.operational = Operational(keys_admins, place)

    # Gets --------------------------------------------------------------------------------------

    @property
    def place(self):
        return self.operational.get_place()

    @property
    def id(self):
        return self.id_machine

    # Operacoes  -------------------------------------------------------------------------------

    def initial_screen(self) -> None:
        while (1):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("========================================================================")
            print("|                      Bem vindo a nossa cafeteria                     |")
            print("========================================================================\n")
            tipo_bebida : str = input("Qual tipo de bebida deseja comprar hoje? (Lata, Dosada)\n").lower()
            if tipo_bebida == "dosada" or tipo_bebida == "lata":
                self.operational.buy_drink(tipo_bebida)
            elif tipo_bebida.upper() == "SAIR":
                exit(0)
            elif tipo_bebida == "codigo_secreto":
                print("\nOla usuario, selecione uma das opcoes abaixo:")
                print("1 - Atualizar Estoque (Permissao exigida: repositor)")
                print("2 - Registrar Bebida Dosada (Permissao exigida: repositor)")
                print("3 - Definir Localizacao da Maquina (Permissao exigida: ADM)")
                print("4 - Consultar Dados (Permissao exigida: ADM)")
                print("5 - Cadastrar Novo Usuario (Permissao exigida: ADM)\n")
                opcao : str = input()

                usuario : str = input("Informe o id de usuario: ")
                senha : str = input("Informe a senha: ")
                if self.operational.users.validate_user(usuario, senha):
                    match opcao:
                        case '1':
                            self.operational.update_stock(usuario, senha)
                        case '2':
                            self.operational.registrar_bebida_dosada(usuario, senha)
                        case '3':
                            self.operational.set_place(usuario, senha)
                        case '4':
                            print("\nSelecione o que pretende consultar:")
                            print("1 - Valor total de vendas")
                            print("2 - Valor de vendas de latas")
                            print("3 - Valor de vendas de bebidas dosadas")
                            print("4 - Quantidade de vendas total\n")
                            sub_op : str = input()
                            match sub_op:
                                case '1':
                                    print(f"R${self.operational.get_total_sales(usuario, senha)},00")
                                case '2':
                                    print(f"R${self.operational.get_can_sales(usuario, senha)},00")
                                case '3':
                                    print(f"R${self.operational.get_dosed_sales(usuario, senha)},00")
                                case '4':
                                    print(f"Quantidade: {self.operational.get_balance(usuario, senha)}")
                        case '5':
                            new_usr : str = input("ID do novo usuario: ")
                            new_password : str = input("Senha do novo usuario: ")
                            new_nvl_acesso : str = input("Nivel de acesso do novo usuario(0 - repositor, 1 - ADM): ")
                            self.operational.cadastrar_usuario(usuario, senha, new_usr, new_password, new_nvl_acesso)
                elif opcao == "hackear_maquina_67":
                    print(self.operational.users.keys)
            input("\nOperacao finalizada, pressione qualquer tecla para continuar...")
