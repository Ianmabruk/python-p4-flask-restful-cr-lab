import pytest
from models import db, Plant

def test_can_be_created(test_app):
    """Can create records that can be committed to the database."""
    with test_app.app_context():
        p = Plant(
            name="Douglas Fir",
            image="https://example.com/douglas.jpg",
            price=12.50
        )
        db.session.add(p)
        db.session.commit()

        retrieved = Plant.query.get(p.id)
        assert retrieved is not None
        assert retrieved.name == "Douglas Fir"
        assert retrieved.image == "https://example.com/douglas.jpg"
        assert retrieved.price == 12.50
