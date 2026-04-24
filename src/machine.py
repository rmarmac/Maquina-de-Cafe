import hashlib

IDX_KEY = 0
IDX_ACESSO = 1

def hashing(string):
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()

class Machine:
    def __init__(self, id_machine:int, status:bool, place:str, keys_admins:dict):
        self.id_machine = id_machine
        self.operational = status
        self.place = place
        self.keys = keys_admins
        for user_id in self.keys:
            self.keys[user_id][IDX_KEY] = hashing(self.keys[user_id][IDX_KEY])

    # Gets --------------------------------------------------------------------------------------

    def get_place(self):
        return self.place
    
    def get_id(self):
        return self.id
    
    def get_key(self, id_usuario):
        return self.keys[id_usuario][IDX_KEY]
    
    def get_permission(self, id_usuario):
        return self.keys[id_usuario][IDX_ACESSO]
    
    # Validacoes  -------------------------------------------------------------------------------

    def validate_usuario(self, id_usuario : int, key : str):
        if not id_usuario in self.keys.keys():
            return False
        if hashing(key) == self.get_key(id_usuario):
            return True
        return False
    
    def cadastrar_usuario(self, id_usr_existente : int, key_usr_exist : str,
                          novo_id : int, nova_senha : str, nvl_acesso : int):
        if not self.validate_usuario(id_usr_existente, key_usr_exist):
            print("Tentativa de acesso negada!\n")
            return False
        if self.keys[id_usr_existente][IDX_ACESSO] == 0:
            print("Nivel de acesso incompativel.")
            return False
        if novo_id in self.keys.keys():
            print("Usuario ja cadastrado")
            return False
        else:
            self.keys[novo_id] = [hashing(nova_senha), nvl_acesso]
            return True

    # Operacoes  -------------------------------------------------------------------------------

    def initial_screen():
        pass

    def buy_drink():
        pass