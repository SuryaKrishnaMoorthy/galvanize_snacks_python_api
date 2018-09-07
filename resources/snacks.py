from flask_restful import Resource, reqparse
import random
from models.snacks import SnacksModel

class Snack(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('name',
                        type=str,
                        required=False
                        )
    parser.add_argument('description',
                        type=str,
                        required=False
                        )
    parser.add_argument('price',
                        type=float,
                        required=False
                        )
    parser.add_argument('img',
                        type=str,
                        required=False
                        )
    parser.add_argument('is_perishable',
                        type=bool,
                        required=False
                        )

    def get(self, id):
        snack = SnacksModel.find_by_snackid(id)
        if snack:
            return snack.json()
        return {'message': 'snack not found'}, 404

    def post(self):
        data = self.parser.parse_args()

        if data is None or data['name'] is None or data['description'] is None or data['price'] is None or data['img'] is None or data['is_perishable'] is None:
            return {'message': 'name, description, price, img and is_perishable fields are required'}

        if SnacksModel.find_by_snackname(data['name']):
            return {'message': "A Snack with name '{}' already exists.".format(data['name'])}, 400

        snack = SnacksModel(**data)
        try:
            snack.save_to_db()
        except:
            return {"message": "An error occurred creating the snack."}, 500

        return snack.json(), 201

    def put(self, id):
        data = self.parser.parse_args()

        if data is None or (data['name'] is None and data['description'] is None and data['price'] is None and data['img'] is None and data['is_perishable'] is None):
            return {'message': 'name/description/price/img/is_perishable field is required'}

        snack = SnacksModel.find_by_snackid(id)

        if snack:
            if data['name']:
                snack.name = data['name']
            if data['description']:
                snack.description = data['description']
            if data['price']:
                snack.price = data['price']
            if data['img']:
                snack.img = data['img']
            if data['is_perishable']:
                snack.is_perishable = data['is_perishable']
        else:
            return {"message": "A Snack with id '{}' does not exist.".format(id)}, 500

        snack.save_to_db()
        return snack.json()

    def delete(self, id):
        snack = SnacksModel.find_by_snackid(id)
        if snack:
            snack.delete_from_db()
            return {'message': 'Snack deleted'}
        else:
            return {'message': 'Snack could not be found'}


class Snacks(Resource):
    def get(self):
        return {'snacks': [snack.json() for snack in SnacksModel.find_all()]}

class SnacksFeatured(Resource):
    def get(self):
        snacks = [snack.json() for snack in SnacksModel.find_all()]
        random_indices = random.sample(range(0, len(snacks)-1), 3)
        featured_snacks = [snacks[random_indices[0]], snacks[random_indices[1]], snacks[random_indices[2]]]
        return {'data': featured_snacks}
