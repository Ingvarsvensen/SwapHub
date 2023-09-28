import database
from generic_wrapper import fetch_top_pools


def main():
    database.create_table()

    # Fetch top 10 pools from Uniswap
    uniswap_data = fetch_top_pools('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3')
    print("Uniswap Data:", uniswap_data)  # Debugging line

    top_10_uniswap = uniswap_data['data']['pools'][:10]
    uniswap_dict = {}
    for pool in top_10_uniswap:
        token_pair = f"{pool['token0']['symbol']}/{pool['token1']['symbol']}"
        uniswap_dict[token_pair] = pool['liquidity']
    database.insert_prices("Uniswap", uniswap_dict)

    # Fetch top 10 pools from PancakeSwap
    pancake_data = fetch_top_pools('https://api.thegraph.com/subgraphs/name/pancakeswap/exchange-v3-bsc')
    print("Pancake Data:", pancake_data)  # Debugging line

    top_10_pancake = pancake_data['data']['pools'][:10]
    pancake_dict = {}
    for pool in top_10_pancake:
        token_pair = f"{pool['token0']['symbol']}/{pool['token1']['symbol']}"
        pancake_dict[token_pair] = pool['liquidity']
    database.insert_prices("PancakeSwap", pancake_dict)

    # Fetch and display rates
    rates = database.fetch_rates()
    print(f"Current rates in database: {rates}")


if __name__ == "__main__":
    main()
