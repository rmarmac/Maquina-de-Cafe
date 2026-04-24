# ☕ Coffee Machine Simulator (POO)

Este projeto simula o funcionamento interno de uma máquina de café automática, aplicando conceitos de **Programação Orientada a Objetos (POO)** em Python.

## 🚀 Objetivo
O objetivo é gerenciar recursos (água, leite, café), processar pagamentos e entregar bebidas baseadas na escolha do usuário, garantindo que o estado da máquina seja atualizado corretamente após cada transação.

## 🛠️ Estrutura de Classes
O projeto foi dividido em classes distintas para garantir a modularidade:

* **`MenuItem`**: Modela cada tipo de bebida (nome, custo e ingredientes).
* **`Menu`**: Gerencia a lista de bebidas disponíveis.
* **`CoffeeMaker`**: Controla os recursos da máquina (água, leite, café) e o preparo das bebidas.
* **`MoneyMachine`**: Responsável pelo processamento de moedas e controle de lucro.

## 📊 Diagrama do Projeto
Abaixo está a representação visual da arquitetura de classes:

![Diagrama de Classes](caminho/para/sua/imagem.png)

## 💻 Como Executar
1. Certifique-se de ter o Python 3 instalado.
2. Clone o repositório.
3. Execute o arquivo principal:
   ```bash
   python main.py
