import psycopg2


def init_db():
    conn = psycopg2.connect(
        host="localhost",
        database="psdb1",
        user="postgres",
        password="psdb11@@!#",
        port=5432
    )
    return conn


def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS token_prices (
        id SERIAL PRIMARY KEY,
        exchange_name TEXT,
        token_symbol TEXT,
        price NUMERIC
    );
    '''
    conn = init_db()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()


def insert_prices(exchange_name, token_data):
    conn = init_db()
    cur = conn.cursor()
    for token, price in token_data.items():
        cur.execute("INSERT INTO token_prices (exchange_name, token_symbol, price) VALUES (%s, %s, %s)",
                    (exchange_name, token, price))
    conn.commit()
    cur.close()
    conn.close()

def fetch_rates():
    conn = init_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM token_prices")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
