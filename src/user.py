import hashlib

IDX_PASS : int = 0
IDX_NVL_ACESSO : int = 1


def hashing(string : str) -> str:
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()


'''
Nivel de acesso do usuario: 0 = repositor de estoque, 1 = administrativo

Padrao de keys para definir um usuario:

    keys_admins
      |
--> admins = {
-->     "renan123": ("senha123",1)
--> }
            |           |       |
           user       senha   nivel de acesso

'''


class Users:
    def __init__(self, keys_iniciais: dict[str, list[str, int]]):
        self.keys : dict[str, list[str, int]] = dict()
        for user in keys_iniciais:
            self.keys[hashing(user)] = [hashing(keys_iniciais[user][IDX_PASS]), keys_iniciais[user][IDX_NVL_ACESSO]]

    def get_password(self, user : str):
        return self.keys[hashing(user)][IDX_PASS]

    def get_nvl_acesso(self, user : str):
        return self.keys[hashing(user)][IDX_NVL_ACESSO]

    def validate_user(self, user: str, password: str) -> bool:
        if not hashing(user) in self.keys.keys():
            return False
        if hashing(password) == self.get_password(user):
            return True
        return False

    # Usuarios com nivel de acesso 1, ja cadastrados, podem cadastrar novos usuarios
    def cadastrar_user(self, usr_exist: str, password_usr_exist: str,
                       new_usr: str, new_password: str, nvl_acesso: int) -> bool:
        if not self.validate_user(usr_exist, password_usr_exist):
            print("Tentativa de acesso negada!\n")
            return False
        if self.get_nvl_acesso(usr_exist) == 0:
            print("Nivel de acesso incompativel.")
            return False
        if hashing(new_usr) in self.keys.keys():
            print("user ja cadastrado")
            return False
        else:
            self.keys[hashing(new_usr)] = [hashing(new_password), nvl_acesso]
            return True