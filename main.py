from src.machine import Machine

def main():
    # Teste de cadastro de usuário na máquina e exemplo de uso ======================================
    admins = {
        "renan123" : ["senha123",0]
    }
    maquina = Machine(0, "sao paulo", admins)
    while(1):
        maquina.operational.update_stock("renan123", "senha123")


if __name__ == "__main__":
    main()