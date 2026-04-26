from src.machine import Machine

def main():
    # Teste de cadastro de usuário na máquina e exemplo de uso ======================================
    admins = {
        "renan123" : ["senha123",0],
        "luiz" : ["senha", 1]
    }
    maquina = Machine(0, "sao paulo", admins)

    maquina.initial_screen()


if __name__ == "__main__":
    main()