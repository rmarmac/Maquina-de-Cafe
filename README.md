content = """# ☕ Simulador de Máquina de Café e Multibebidas (POO)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Paradigma](https://img.shields.io/badge/Paradigma-POO-success.svg)]()
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange.svg)]()

## 📌 I. Introdução
Este projeto é uma aplicação desenvolvida em **Python** utilizando os conceitos de **Programação Orientada a Objetos (POO)**. O objetivo é simular o funcionamento de uma máquina automática de café e bebidas não alcoólicas, aplicando conceitos de abstração, encapsulamento, herança e polimorfismo.

O sistema foi inicialmente modelado em UML e refinado para garantir uma separação de responsabilidades eficiente, focando em segurança de dados e controle de acesso por níveis de permissão.

---

## ⚙️ II. Descrição do Sistema e Funcionalidades

A máquina opera em dois modos: o modo **Cliente** (venda direta) e o modo **Administrativo/Operacional** (gerenciamento).

### 🥤 Tipos de Bebidas
O sistema fornece dois tipos principais de produtos, agora centralizados sob a classe `Drink`:

1. **Bebidas Dosadas (`DosedDrink`):**
   * Bebidas quentes feitas sob demanda (ex: café, leite, açúcar).
   * **Customização:** O usuário escolhe a dosagem dos ingredientes: **30%, 50%, 70% ou 100%**.
   * O estoque de insumos é deduzido proporcionalmente à dose escolhida.

2. **Bebidas em Lata (`CannedDrink`):**
   * Bebidas geladas prontas para consumo.
   * O estoque é contabilizado por unidade.

### 💳 Formas de Pagamento
Suporta modalidades simuladas como Pix, Cartão de Crédito e Débito.

### 🔐 Controle de Acesso e Níveis de Usuário
A interação com a máquina varia conforme o perfil:

* **Cliente Regular:** Não necessita de login ou fornecimento de dados. Pode comprar qualquer bebida disponível livremente.
* **Usuários do Sistema (Repositores e Administradores):** Para acessar as funções internas, o usuário deve inserir uma **chave secreta padrão**. Uma vez validada a chave, o sistema solicita login e senha para verificar o nível de acesso no dicionário criptografado:
    * **Nível 0 (Repositor):** Permissão para reabastecer o estoque de ingredientes e latas.
    * **Nível 1 (Administrador):** Permissão total, incluindo visualização de balanço financeiro e relatórios de vendas.

### 🏴‍☠️ Simulação de Hacker
O projeto inclui uma funcionalidade de simulação de invasão. Nela, um "hacker" consegue acessar e exibir o dicionário de usuários do sistema. O objetivo é demonstrar que, embora os dados brutos sejam acessados, as senhas permanecem protegidas via hash **SHA-256**, impedindo o acesso efetivo às contas.

---

## 🏗️ Arquitetura e Mudanças no Diagrama

A arquitetura foi simplificada em relação ao modelo inicial para melhorar a manutenção do código:

### Principais Alterações:
* **Associação de Bebidas:** A classe `Drink` (e suas herdeiras `CannedDrink` e `DosedDrink`) agora está associada diretamente à parte **`Operational`** da máquina, e não mais à `Machine`.
* **Unificação de Tipos:** A classe `DrinkType` foi removida, sendo substituída diretamente pela estrutura da classe `Drink`.
* **Simplificação de Usuários:** As classes `UserAccount`, `Manager` e `Stocker` foram descontinuadas. Agora existe apenas a classe **`Users`**. Os papéis (Repositor/ADM) são definidos por um atributo de nível de acesso (0 ou 1) dentro de um dicionário seguro.

---

## 🚀 Como Executar o Projeto

**Pré-requisitos:** Python 3.8 ou superior.

1. Clone o repositório:
   ```bash
   git clone [https://github.com/rmarmac/Maquina-de-Cafe.git](https://github.com/rmarmac/Maquina-de-Cafe.git)