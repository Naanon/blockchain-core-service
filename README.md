
# Blockchain Core Service

  - [1. Project Description](#1-project-description)
  - [2. Features](#2-features)
  - [3. Technologies Used](#3-technologies-used)
  - [4. Prerequisites](#4-prerequisites)
  - [5. Installation](#5-installation)
    - [5.1. Clone the Repository](#51-clone-the-repository)
    - [5.2. Access the Project Directory](#52-access-the-project-directory)
    - [5.3. Create and Activate the Virtual Environment](#53-create-and-activate-the-virtual-environment)
    - [5.4. Install Dependencies](#54-install-dependencies)
  - [6. Execution](#6-execution)
    - [6.1. Configure Environment Variables](#61-configure-environment-variables)
    - [6.2. Start the Application](#62-start-the-application)
    - [6.3. Swagger UI](#63-swagger-ui)
    - [6.4. Sepolia Testnet Explorer](#64-sepolia-testnet-explorer)
  - [7. API Endpoints](#7-api-endpoints)
    - [7.1. Address Management](#71-address-management)
    - [7.2. Transaction Validation](#72-transaction-validation)
    - [7.3. Transaction Sending](#73-transaction-sending)

## 1. Project Description
RESTful API developed in Python for interaction with the Ethereum blockchain network. The service allows generating and storing new wallets, validating incoming transactions (identifying ETH or ERC-20 tokens), and creating on-chain outbound transactions. The entire operation history is stored for future reference.

## 2. Features
* **Wallet Management:** Generates new Ethereum addresses and stores them in a local database for future use.
* **Transaction Validation:** Validates on-chain transactions to confirm the secure receipt of funds. The system identifies the transferred asset (ETH or ERC-20 tokens) and verifies whether the destination is one of the managed wallets.
* **Transaction Creation:** Sends new transactions from a managed wallet, including network fee calculation, signing, and monitoring until confirmation by the network.
* **Traceability:** Stores detailed history for both incoming and outgoing transactions, ensuring control and efficiency in traceability.

## 3. Technologies Used
* **Python 3.8+**
* **FastAPI:** For building the REST API.
* **Web3.py:** For interactions with the Ethereum network.
* **SQLAlchemy:** For communication with the database.
* **SQLite:** As a local database.

## 4. Prerequisites
* **Python 3.8+**
* An account with a node service. For this project, the following public **Infura** URL for the Sepolia testnet was used: `https://sepolia.infura.io/v3/42bff0d9dc884f93808b09d696b2b21a`.

## 5. Installation
### 5.1. Clone the Repository
```sh
git clone https://github.com/Naanon/blockchain-core-service.git
```

### 5.2. Access the Project Directory
```sh
cd blockchain-core-service
```

### 5.3. Create and Activate the Virtual Environment
* **On Windows:**

```sh
python -m venv venv
.env\Scriptsctivate
```

* **On macOS / Linux:**
```sh
python3 -m venv venv
source venv/bin/activate
```

### 5.4. Install Dependencies
```sh
pip install -r requirements.txt
```

## 6. Execution
### 6.1. Configure Environment Variables
* **Rename the .env.example file located at the root of the project to .env**

### 6.2. Start the Application
```sh
uvicorn app.app:app --reload
```

### 6.3. Swagger UI
* The application's Swagger UI can be accessed at **http://127.0.0.1:8000/docs**

### 6.4. Sepolia Testnet Explorer
* Transaction validation can be performed through **https://sepolia.etherscan.io/**

## 7. API Endpoints
### 7.1. Address Management
* **POST /wallets:** Generates a specified number of new addresses.
* **GET /wallets:** Retrieves the list of all generated addresses.

### 7.2. Transaction Validation
* **POST /transactions/validate:** Validates an on-chain transaction hash to generate credit.
* **GET /transactions/history:** Retrieves the history of validated incoming transactions.

### 7.3. Transaction Sending
* **POST /transactions/send:** Creates and sends a new on-chain transaction.
* **GET /transactions/outgoing:** Retrieves the history of outbound transactions initiated by the system.
