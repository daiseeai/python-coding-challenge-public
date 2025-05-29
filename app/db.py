"""This module spins up a dummy `test.db` in the root of the project if it does not exist.

The data within this is created using `Faker` and will be random in nature.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from faker import Faker
import random

# Use SQLite for easy testing
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    """Creates `test.db` at local path.

    Populates if it does not already exist. OR it's empty.
    """
    # Create all tables first
    Base.metadata.create_all(bind=engine)

    # Add sample data if the database is empty
    db = SessionLocal()
    try:
        # NOTE: Why are we importing `Product` here?
        # What issues could this cause?
        from .models import Product

        # Check if we have any products
        if db.query(Product).first() is None:
            fake = Faker(["en_US"])
            categories = [
                "Electronics",
                "Clothing",
                "Books",
                "Home & Garden",
                "Sports",
                "Beauty",
                "Toys",
                "Automotive",
                "Health",
                "Jewelry",
            ]

            # Generate 100 random products
            # NOTE: highly random in nature. May not be actual "realistic examples"
            products = []
            for _ in range(100):
                product = Product(
                    name=fake.catch_phrase(),
                    description=fake.text(max_nb_chars=200),
                    price=round(random.uniform(10.0, 1000.0), 2),
                    category=random.choice(categories),
                    stock=random.randint(0, 100),
                )
                products.append(product)

            db.add_all(products)
            db.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
