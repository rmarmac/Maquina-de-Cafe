from src.machine import Machine

def main():
    # Teste de cadastro de usuário na máquina --------------------------------------
    admins = {
        1 : ["senha123",1]
    }

    maquina = Machine(0, True, "sao paulo", admins)
    maquina.cadastrar_usuario(1, "senha123", 2, "senha12", 1)
    print(maquina.validate_usuario(2, "senha12"))

    # Teste de cadastro de usuário na máquina --------------------------------------




if __name__ == "__main__":
    main()