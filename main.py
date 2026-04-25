from src.machine import Machine

def main():
    # Teste de cadastro de usuário na máquina --------------------------------------
    admins = {
        1 : ["senha123",1]
    }

    maquina = Machine(0, "sao paulo", admins)



if __name__ == "__main__":
    main()