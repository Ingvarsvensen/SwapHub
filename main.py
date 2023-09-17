import database

database.create_table()

database.insert_rate("Uniswap", "ETH/DAI", 2000)  # Пример данных

rates = database.fetch_rates()
