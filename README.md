# Blockchain Core Service
<img height="50" width="50" alt="Python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" /> <img height="50" width="50" alt="FastAPI" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg" /> <img height="50" width="50" alt="SQLAlchemy" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original.svg" /> <img height="50" width="50" alt="SQLite" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original.svg" />

  - [1. Descrição do Projeto](#1-descrição-do-projeto)
  - [2. Funcionalidades](#2-funcionalidades)
  - [3. Tecnologias Utilizadas](#3-tecnologias-utilizadas)
  - [4. Pré-requisitos](#4-pré-requisitos)
  - [5. Instalação](#5-instalação)
  - [6. Execução](#6-execução)
  - [7. Endpoints da API](#7-endpoints-da-api)
    - [7.1. Gerenciamento de Endereços](#71-gerenciamento-de-endereços)
    - [7.2. Validação de Transações](#72-validação-de-transações)
    - [7.3. Envio de Transações](#73-envio-de-transações)

## 1. Descrição do Projeto
API REST desenvolvida com Python para interação com a rede blockchain Ethereum. O projeto permite criar e armazenar novas carteiras, validar transações de recebimento (identificando ETH ou tokens ERC-20) e criar transações de envio on-chain. Todo o histórico de operações é armazenado para posterior consulta.

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
* Uma conta em um serviço de nós, como **Infura** ou **Alchemy**, para obter uma URL de acesso a um nó da rede de testes Sepolia.

## 5. Instalação
### 5.1. Clone o Repositório
   ```sh
   git clone <URL_DO_SEU_REPOSITORIO_GIT>
