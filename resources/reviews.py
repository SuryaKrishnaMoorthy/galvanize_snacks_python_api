from flask_restful import Resource, reqparse
from models.reviews import ReviewModel
from models.snacks import SnacksModel

class Review(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('title',
                        type=str,
                        required=False
                        )

    parser.add_argument('text',
                        type=str,
                        required=False
                        )

    parser.add_argument('rating',
                        type=float,
                        required=False
                        )

    def get(self, snack_id, id):
        review = ReviewModel.find_by_review_id(id)
        if review:
            review_json = review.json()
            if review_json['snack_id'] != snack_id:
                return {'message': 'No such review for this snack id'}, 404
            return review_json
        return {'message': 'review not found'}, 404

    def put(self, snack_id, id):
        if SnacksModel.find_by_snackid(snack_id) is None:
            return {'message': "A snack with id '{}' does not exists.".format(snack_id)}, 400

        data = self.parser.parse_args()
        if data is None or (data['title'] is None and data['text'] is None and data['rating'] is None):
            return {'message': 'title/text/rating field is required'}

        review = ReviewModel.find_by_review_id(id)

        if review:
            if data['title']:
                review.title = data['title']
            if data['text']:
                review.text = data['text']
            if data['rating']:
                review.rating = data['rating']
        else:
            return {'message': 'Review not found'}, 404

        review.save_to_db()

        return review.json()

    def delete(self, snack_id, id):
        if SnacksModel.find_by_snackid(snack_id) is None:
            return {'message': "A snack with id '{}' does not exists.".format(snack_id)}, 400

        review = ReviewModel.find_by_review_id(id)

        if review:
            review.delete_from_db()
            return {'message': 'Review deleted.'}
        return {'message': 'Review not found.'}, 404

class Reviews(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('title',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('text',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('rating',
                        type=float,
                        required=True,
                        help="Every item needs a id."
                        )

    def get(self, snack_id):
        return {'reviews': [review.json() for review in ReviewModel.find_all(snack_id)]}

    def post(self, snack_id):
        if SnacksModel.find_by_snackid(snack_id) is None:
            return {'message': "A snack with id '{}' does not exists.".format(snack_id)}, 400

        data = self.parser.parse_args()
        review = ReviewModel(data['title'], data['text'], data['rating'], snack_id)

        try:
            review.save_to_db()
        except:
            return {"message": "An error occurred while creating the review."}, 500

        return review.json(), 201
