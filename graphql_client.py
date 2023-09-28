import json

from graphqlclient import GraphQLClient


def fetch_token_prices(endpoint):
    client = GraphQLClient(endpoint)
    result = client.execute('''
    {
        pools(first: 100, orderBy: liquidity, orderDirection: desc) {
            id
            liquidity
            token0 {
                id
                symbol
            }
            token1 {
                id
                symbol
            }
        }
    }
    ''')

    print("Raw GraphQL Response:", result)  # Debugging line

    data = json.loads(result)

    if 'data' not in data or 'pools' not in data['data']:
        print("Unexpected GraphQL response structure.")
        return {}

    token_pools = {}
    for item in data['data']['pools']:
        token0_symbol = item['token0']['symbol']
        token1_symbol = item['token1']['symbol']
        liquidity = item['liquidity']

        token_pools[f"{token0_symbol}/{token1_symbol}"] = liquidity

    return token_pools
