from web3 import Web3

# Инициализация Web3
w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

# Адрес и ABI смарт-контракта PancakeSwap
contract_address = '0x...'  # Замените на реальный адрес
contract_abi = [...]  # Замените на реальный ABI

# Инициализация контракта
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Получение данных
token_price = contract.functions.getPrice().call()  # Этот метод зависит от контракта

# Вставка данных в таблицу
database.insert_rate("PancakeSwap", "TOKEN/BNB", token_price)
