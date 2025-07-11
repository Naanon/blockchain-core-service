# Blockchain Core Service
<img height="50" width="50" alt="Python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" /> <img height="50" width="50" alt="FastAPI" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg" /> <img height="50" width="50" alt="SQLAlchemy" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original.svg" /> <img height="50" width="50" alt="SQLite" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original.svg" />

  - [1. Descrição do Projeto](#1-descrição-do-projeto)
  - [2. Funcionalidades](#2-funcionalidades)
  - [3. Tecnologias Utilizadas](#3-tecnologias-utilizadas)
  - [4. Pré-requisitos](#4-pré-requisitos)
  - [5. Instalação](#5-instalação)
    - [5.1. Clone o Repositório](#51-clone-o-repositório)
    - [5.2. Acesse o diretório do projeto](#52-acesse-o-diretório-do-projeto)
    - [5.3. Crie e Ative o Ambiente Virtual](#53-crie-e-ative-o-ambiente-virtual)
    - [5.4. Instale as Dependências](#54-instale-as-dependências)
  - [6. Execução](#6-execução)
    - [6.1. Configure as Variáveis de Ambiente](#61-configure-as-variáveis-de-ambiente)
    - [6.2. Inicie a Aplicação](#62-inicie-a-aplicação)
  - [7. Endpoints da API](#7-endpoints-da-api)
    - [7.1. Gerenciamento de Endereços](#71-gerenciamento-de-endereços)
    - [7.2. Validação de Transações](#72-validação-de-transações)
    - [7.3. Envio de Transações](#73-envio-de-transações)

## 1. Descrição do Projeto
API RESTful desenvolvida em Python para interação com a rede blockchain Ethereum. O serviço permite gerar e armazenar novas carteiras, validar transações de recebimento (identificando ETH ou tokens ERC-20) e criar transações de envio on-chain. Todo o histórico de operações é armazenado para consulta.

## 2. Funcionalidades
* **Gerenciamento de Carteiras:** Geração de novos endereços Ethereum com armazenamento em um banco de dados local para uso futuro.
* **Validação de Transações:** Validação de transações on-chain para confirmar o recebimento seguro de fundos. O sistema identifica o ativo transferido (ETH ou Tokens ERC-20) e verifica se o destino é uma das carteiras gerenciadas.
* **Criação de Transações:** Envio de novas transações a partir de uma carteira gerenciada, incluindo cálculo de taxa de rede, assinatura e monitoramento até a confirmação pela rede.
* **Rastreabilidade:** Armazenamento de histórico detalhado para transações de entrada e saída, garantindo controle e eficácia na rastreabilidade.

## 3. Tecnologias Utilizadas
* **Python 3.8+**
* **FastAPI:** Para a construção da API REST.
* **Web3.py:** Para interações com a rede Ethereum.
* **SQLAlchemy:** Para a comunicação com o banco de dados.
* **SQLite:** Como banco de dados local.

## 4. Pré-requisitos
* **Python 3.8+**
* **Git**
* Uma conta em um serviço de nós, como **Infura** ou **Alchemy**. Para este projeto, foi utilizada a seguinte URL pública do Infura para a rede de testes Sepolia: `https://sepolia.infura.io/v3/42bff0d9dc884f93808b09d696b2b21a`.

## 5. Instalação
### 5.1. Clone o Repositório
   ```sh
   git clone https://github.com/Naanon/blockchain-core-service.git
   ```
### 5.2. Acesse o Diretório do Projeto
   ```sh
   cd blockchain-core-service
   ```
### 5.3. Crie e Ative o Ambiente Virtual
* **No Windows:**
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```
* **No macOS / Linux:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
### 5.4. Instale as Dependências
   ```sh
   pip install -r requirements.txt
   ```

## 6. Execução
### 6.1. Configuração das Variáveis de Ambiente
* **Renomeie o arquivo .env.example situado na raiz do projeto para .env**
### 6.2. Inicie a Aplicação
   ```sh
   uvicorn app.app:app --reload
   ```

## 7. Endpoints da API
### 7.1. Gerenciamento de Endereços
* **POST /wallets:** Gera uma quantidade especificada de novos endereços.
* **GET /wallets:** Consulta a lista de todos os endereços gerados.
### 7.2. Validação de Transações
* **POST /transactions/validate:** Valida um hash de transação on-chain para gerar crédito.
* **GET /transactions/history:** Consulta o histórico de transações de recebimento validadas.
### 7.3. Envio de Transações
* **POST /transactions/send:** Cria e envia uma nova transação on-chain.
* **GET /transactions/outgoing:** Consulta o histórico de transações de envio iniciadas pelo sistema.
