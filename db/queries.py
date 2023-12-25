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
        DROP TABLE IF EXISTS category
        """
    )
    cursor.execute(
        """
        DROP TABLE IF EXISTS products
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price DECIMAL,
            image TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category (id)
        )
        """
    )
    db.commit()


def populate_tables():
    cursor.execute(
        """
        INSERT INTO category (name) VALUES
        ("Книги"), ("Манги"), ("Сувениры")
        """
    )
    cursor.execute(
        """
        INSERT INTO products(name, price, image, category_id) VALUES
    ('Алхимик', 560.00, 'images/book1.jpg', 1),
    ('Майкл Джордан. Его воздушество', 1650.00, 'images/book2.jpg', 1),
    ('Генри Форд. Моя жизнь, мои достижения', 1200.00, 'images/book3.jpg', 1),
    ('Графические романы. Наруто. Книга 1', 920.00, 'images/manga1.jpg', 2),
    ('Графические романы. Наруто. Книга 2', 920.00, 'images/manga2.jpg', 2),
    ('Закладки для книг', 25.00, 'images/souvenirs.jpg', 3)
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


def get_product_by_category_id(category_id: int):
    cursor.execute(
        """
        SELECT * FROM products WHERE category_id = :cat_id
        """, {"cat_id": category_id}
    )
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    # pprint(get_all_products())
    pprint(get_product_by_category_id(2))

