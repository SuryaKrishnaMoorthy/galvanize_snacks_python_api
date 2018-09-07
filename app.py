from flask import Flask
from flask_restful import Api
from resources.snacks import Snacks, Snack, SnacksFeatured
from resources.reviews import Reviews, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/galvanize_snacks_python_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

snack_routes = [
    '/snacks',
    '/snacks/<int:id>'
]

api.add_resource(Snacks, '/snacks')
api.add_resource(SnacksFeatured, '/snacks/featured')
api.add_resource(Snack, *snack_routes)
api.add_resource(Reviews, '/snacks/<int:snack_id>/reviews')
api.add_resource(Review, '/snacks/<int:snack_id>/reviews/<int:id>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
