# server/seed.py

from app import app
from models import db, Plant

def seed_plants():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()

        # Clear table
        db.session.query(Plant).delete()

        # Seed data
        plants = [
            Plant(name="Aloe", image="https://images.unsplash.com/photo-1617196039957-7d0fa0c6c0aa", price=11.50),
            Plant(name="ZZ Plant", image="https://images.unsplash.com/photo-1599058917218-2b6225fa0f2c", price=25.98),
            Plant(name="Snake Plant", image="https://images.unsplash.com/photo-1626825567981-b9f7d1f76c12", price=15.75),
            Plant(name="Fiddle Leaf Fig", image="https://images.unsplash.com/photo-1587302452322-8d0d50a46f70", price=45.00),
        ]

        db.session.add_all(plants)
        db.session.commit()
        print("Database seeded with plants!")

if __name__ == "__main__":
    seed_plants()
