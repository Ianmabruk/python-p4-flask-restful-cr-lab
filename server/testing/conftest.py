import pytest
from app import app
from models import db

@pytest.fixture(scope="function")
def test_app():
    """Provides a test app with an in-memory database."""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()      # Create tables
        yield app
        db.session.remove()
        db.drop_all()        # Clean up
