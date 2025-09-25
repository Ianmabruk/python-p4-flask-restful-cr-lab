import json
from models import db, Plant

def test_plants_get_route(test_app):
    """Has a resource available at '/plants'."""
    client = test_app.test_client()
    response = client.get('/plants')
    assert response.status_code == 200

def test_plants_get_route_returns_list_of_plant_objects(test_app):
    """Returns JSON representing Plant objects at '/plants'."""
    with test_app.app_context():
        p = Plant(
            name="Douglas Fir",
            image="https://example.com/douglas.jpg",
            price=12.50
        )
        db.session.add(p)
        db.session.commit()

        client = test_app.test_client()
        response = client.get('/plants')
        data = json.loads(response.data.decode())
        assert type(data) == list
        assert len(data) == 1
        assert data[0]['id'] == p.id
        assert data[0]['name'] == p.name

def test_plants_post_route_creates_plant_record_in_db(test_app):
    """Allows creating Plant records through '/plants' POST route."""
    client = test_app.test_client()
    response = client.post(
        '/plants',
        json={
            "name": "Live Oak",
            "image": "https://example.com/liveoak.jpg",
            "price": 250.00
        }
    )

    with test_app.app_context():
        lo = Plant.query.filter_by(name="Live Oak").first()
        assert lo is not None
        assert lo.name == "Live Oak"
        assert lo.image == "https://example.com/liveoak.jpg"
        assert lo.price == 250.00

def test_plant_by_id_get_route(test_app):
    """Has a resource available at '/plants/<int:id>'."""
    with test_app.app_context():
        p = Plant(
            name="Fiddle Leaf Fig",
            image="https://example.com/fig.jpg",
            price=45.00
        )
        db.session.add(p)
        db.session.commit()

        client = test_app.test_client()
        response = client.get(f'/plants/{p.id}')
        assert response.status_code == 200
        data = json.loads(response.data.decode())
        assert data['id'] == p.id
        assert data['name'] == p.name
