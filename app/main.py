from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def home():
    return "Hello world"

# Database Model
class Container(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<Container {self.name}>"

# Flask-Admin
admin = Admin(app, name='Admin', template_mode='bootstrap3')
admin.add_view(ModelView(Container, db.session))

# Database creation if not exist
with app.app_context():
    db.create_all()

@app.route('/containers', methods=['GET'])
def get_containers():
    containers = Container.query.all()
    return jsonify([{"id": c.id, "name": c.name, "status": c.status} for c in containers])

@app.route('/containers', methods=['POST'])
def create_container():
    data = request.get_json()
    new_container = Container(name=data['name'], status=data['status'])
    db.session.add(new_container)
    db.session.commit()
    return jsonify({"message": "Container created"}), 201

# Launch API
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)