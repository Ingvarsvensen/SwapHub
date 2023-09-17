import eth
from web3 import Web3
from uniswap import Uniswap
from dotenv import load_dotenv
import database
import os

from etherscan import Etherscan

#eth_balance = eth.get_eth_balance("0x39eB410144784010b84B076087B073889411F878")
#print(eth_balance)

load_dotenv()

private_key = os.environ["PRIVATE_KEY"]
address = os.environ["ADDRESS"]
provider = os.environ["PROVIDER"]
eth = Etherscan("ETH_API_KEY")
#provider = Web3.HTTPProvider("PROVIDER")

token_address = Web3.to_checksum_address("0x6b175474e89094c44da98b954eedeac495271d0f")  # DAI

#address = Web3.to_checksum_address("0x434e0E580d37B912D6BB87C0942A683E51a7fD36")
uniswap_wrapper = Uniswap(address=address, private_key=private_key, provider=provider)

eth_amount = 1 * 10**18  # 1 ETH в wei
price = uniswap_wrapper.get_price_input("0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE", token_address, eth_amount)


database.create_table()
database.insert_rate("Uniswap", "ETH/DAI", price)
rates = database.fetch_rates()

print(price)
print(rates)

