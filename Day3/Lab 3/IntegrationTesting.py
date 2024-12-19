import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.name for user in users])

# Integration Test
@pytest.fixture
def init_db():
    db.create_all()
    user1 = User(name="John")
    user2 = User(name="Alice")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    yield db
    db.drop_all()

def test_get_users(init_db):
    with app.test_client() as client:
        response = client.get('/users')
        data = response.get_json()
        assert response.status_code == 200
        assert 'John' in data
        assert 'Alice' in data
