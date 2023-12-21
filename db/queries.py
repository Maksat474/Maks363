import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    db_path = Path(__file__).parent.parent / "db/sqlite3"
    global db, cursor
    db = sqlite3.connect(db_path)
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS products
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price DECIMAL,
            image TEXT
        )
        """
    )
    db.commit()


def populate_tables():
    cursor.execute(
        """
        INSERT INTO products (name, price, image) VALUES 
        ('Алхимик', 560.00, 'images/book1.jpg'),
        ('Майкл Джордан. Его воздушество', 1650.00, 'images/book2.jpg'),
        ('Генри Форд. Моя жизнь, мои достижения', 1200.00, 'images/book3.jpg')
        """
    )
    db.commit()


def get_all_products():
    cursor.execute(
        """
        SELECT * FROM products 
        """
    )
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    pprint(get_all_products())
