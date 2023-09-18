from web3 import Web3
from uniswap import Uniswap
from dotenv import load_dotenv
import os
import requests


load_dotenv()
private_key = os.getenv("PRIVATE_KEY")
address = os.getenv("ADDRESS")
provider = os.getenv("PROVIDER")
network = os.getenv("NETWORK", "testnet")  # mainnet по умолчанию, может быть изменено на testnet

# GraphQL requests function
def execute_graphql_query(query):
    url = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3"  # actual endpoint for mainnet
    response = requests.post(url, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to execute GraphQL query. Status code: {response.status_code}")

# Fetching top liquid pools
def get_most_liquid_pools():
    query = """
    {
      pools(first: 1000, orderBy: liquidity, orderDirection: desc) {
        id
      }
    }
    """
    result = execute_graphql_query(query)
    return result['data']['pools']


if network == "mainnet":
    pass
elif network == "testnet":
    pass
else:
    raise ValueError("Invalid network specified")

# Initialize Uniswap
uniswap_wrapper = Uniswap(address=address, private_key=private_key, provider=provider, version=3)

# Getting price of ETH in DAI
eth_address = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"  # ETH
dai_address = "0x6B175474E89094C44Da98b954EedeAC495271d0F"  # DAI

eth_amount = 0.001 * 10**18
try:
    price = uniswap_wrapper.get_price_input(eth_address, dai_address, eth_amount)
    print(f"The price of {eth_amount} ETH in DAI is: {price}")

    most_liquid_pools = get_most_liquid_pools()
    print(f"Most liquid pools: {most_liquid_pools}")

except Exception as e:
    print(f"An error occurred: {e}")
