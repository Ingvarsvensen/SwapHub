from graphqlclient import GraphQLClient
import json


def fetch_top_pools(endpoint):
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
    data = json.loads(result)
    return data
