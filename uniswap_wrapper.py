from graphql_uniswap import fetch_top_tokens
import database
import json

# Fetch top tokens from GraphQL API
top_tokens = fetch_top_tokens()

# Select the first pool as an example (you can choose another one)
first_pool = top_tokens['data']['pools'][0]

# Get the token addresses from the first pool
eth_address = first_pool['token0']['id']
dai_address = first_pool['token1']['id']

# Get the current liquidity of the pool
current_liquidity = first_pool['liquidity']

# Insert the rate and liquidity information into the database
database.insert_rate("Uniswap", f"{first_pool['token0']['symbol']}/{first_pool['token1']['symbol']}", current_liquidity)

# Check if the data was successfully inserted
rates = database.fetch_rates()
print(f"Current rates in database: {rates}")
