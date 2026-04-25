from user import Users

class Machine:
    def __init__(self, id_machine:int, place:str, keys_admins:dict):
        self.id_machine = id_machine
        self.place = place
        

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