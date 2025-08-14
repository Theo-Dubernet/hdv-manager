from .database import get_db
from datetime import datetime

db = get_db()

def insert_sale(name_item, lot, price):
    cur = db.cursor()

    now = datetime.now()

    validate_price = int(price.value)
    validate_lot = int(lot.value)

    cur.execute("""
    INSERT INTO buy_item (lot, price, name_item, date_buy)
        VALUES (%s, %s, %s, %s)
    """, (validate_lot, validate_price, name_item.value, now))

    db.commit()
    cur.close()

def get_all_buy():
    cur = db.cursor()

    cur.execute("SELECT * FROM buy_item order by date_buy desc")

    return cur.fetchall()