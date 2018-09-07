from db import db

class ReviewModel(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    text = db.Column(db.String())
    rating = db.Column(db.Float(precision=2))

    snack_id = db.Column(db.Integer, db.ForeignKey('snacks.id'))
    snack = db.relationship('SnacksModel')

    def __init__(self, title, text, rating, snack_id):
        self.title = title
        self.text = text
        self.rating = rating
        self.snack_id = snack_id

    def json(self):
        return {'id': self.id,'title': self.title, 'text': self.text, 'rating': self.rating, 'snack_id': self.snack_id}

    @classmethod
    def find_all(cls, _id):
        return cls.query.filter_by(snack_id=_id)

    @classmethod
    def find_by_review_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        print('SELF', self.json())
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
