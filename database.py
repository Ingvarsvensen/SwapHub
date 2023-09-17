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
    conn = init_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS currency_rates (
        id SERIAL PRIMARY KEY,
        dex_name TEXT NOT NULL,
        pair TEXT NOT NULL,
        rate NUMERIC(10, 4) NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    cur.close()
    conn.close()


def insert_rate(dex_name, pair, rate):
    conn = init_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO currency_rates (dex_name, pair, rate) VALUES (%s, %s, %s)", (dex_name, pair, rate))
    conn.commit()
    cur.close()
    conn.close()


def fetch_rates():
    conn = init_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM currency_rates")
    rates = cur.fetchall()
    cur.close()
    conn.close()
    return rates
