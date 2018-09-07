from db import db

class SnacksModel(db.Model):
    __tablename__ = 'snacks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String)
    price = db.Column(db.Float(precision=2))
    img = db.Column(db.String)
    is_perishable = db.Column(db.Boolean, nullable=False)

    reviews = db.relationship('ReviewModel', lazy='dynamic')

    def __init__(self, name, description, price, img, is_perishable ):
        self.name = name
        self.description = description
        self.price = price
        self.img = img
        self.is_perishable = is_perishable

    def json(self):
        return { 'id': self.id, 'name': self.name, 'description': self.description, 'price': self.price, 'img': self.img, 'is_perishable': self.is_perishable, 'reviews': [review.json() for review in self.reviews.all()] }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_snackname(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_snackid(cls, _id):
        return cls.query.filter_by(id=_id).first()
