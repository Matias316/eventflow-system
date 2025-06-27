import pytest
from app import create_app
from app.services.db import db

@pytest.fixture
def app():
    app = create_app("testing")

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def http_client(app):
    return app.test_client()
