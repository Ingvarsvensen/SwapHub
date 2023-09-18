from web3 import Web3


w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))


contract_address = '0x...'
contract_abi = [...]


contract = w3.eth.contract(address=contract_address, abi=contract_abi)


token_price = contract.functions.getPrice().call()  # Этот метод зависит от контракта


database.insert_rate("PancakeSwap", "TOKEN/BNB", token_price)
