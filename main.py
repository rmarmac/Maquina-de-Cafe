from src.machine import Machine

def main():
    # Teste de cadastro de usuário na máquina e exemplo de uso ======================================
    admins = {
        "renan123" : ["senha123",0]
    }
    maquina = Machine(0, "sao paulo", admins)

    maquina.operational.update_stock("renan123", "senha123")
    maquina.operational.update_stock("renan123", "senha123")
    maquina.operational.registrar_bebida_dosada("renan123", "senha123")
  
    maquina.operational.buy_drink()


if __name__ == "__main__":
    main()