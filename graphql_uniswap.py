from graphqlclient import GraphQLClient
import json


def fetch_top_tokens():
    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3')

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


if __name__ == "__main__":
    top_tokens = fetch_top_tokens()
    pretty_json_str = json.dumps(top_tokens, indent=4)
    print(pretty_json_str)
