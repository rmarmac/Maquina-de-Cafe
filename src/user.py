import hashlib

IDX_PASS = 0
IDX_NVL_ACESSO = 1

def hashing(string):
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()


class Users:
    def __init__(self, keys_iniciais:dict):
        self.keys = dict()
        for user in keys_iniciais:
            self.keys[hashing(user)] = [hashing(keys_iniciais[user][IDX_PASS]),keys_iniciais[user][IDX_NVL_ACESSO]]

    def get_password(self, user):
        return self.keys[hashing(user)][IDX_PASS]

    def validate_user(self, user:str, password : str):
        if not hashing(user) in self.keys.keys():
            return False
        if hashing(password) == self.get_password(user):
            return True
        return False
    
    def cadastrar_user(self, usr_exist : str, password_usr_exist : str,
                          new_usr : int, new_password : str, nvl_acesso : int):
        if not self.validate_user(usr_exist, password_usr_exist):
            print("Tentativa de acesso negada!\n")
            return False
        if self.keys[hashing(usr_exist)][IDX_NVL_ACESSO] == 0:
            print("Nivel de acesso incompativel.")
            return False
        if hashing(new_usr) in self.keys.keys():
            print("user ja cadastrado")
            return False
        else:
            self.keys[hashing(new_usr)] = [hashing(new_password), nvl_acesso]
            return True
