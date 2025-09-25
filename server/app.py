# server/app.py

import os
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Plant

app = Flask(__name__)

# Ensure the instance folder exists
INSTANCE_PATH = os.path.join(os.path.dirname(__file__), "instance")
os.makedirs(INSTANCE_PATH, exist_ok=True)

# Use absolute path for SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(INSTANCE_PATH, 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# -------------------------
# Routes
# -------------------------

@app.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([p.to_dict() for p in plants])

@app.route('/plants/<int:id>', methods=['GET'])
def get_plant(id):
    plant = Plant.query.get_or_404(id)
    return jsonify(plant.to_dict())

@app.route('/plants', methods=['POST'])
def create_plant():
    data = request.get_json() or {}
    name = data.get('name')
    image = data.get('image')
    price = data.get('price')

    if not name or not image or price is None:
        return jsonify({"errors": ["Missing name, image, or price"]}), 400

    plant = Plant(name=name, image=image, price=price)
    db.session.add(plant)
    db.session.commit()
    return jsonify(plant.to_dict()), 201

if __name__ == "__main__":
    app.run(port=5555, debug=True)
