from . import db

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    count = db.Column(db.String(50))
    point = db.Column(db.Float, nullable=False)
    showAlternative = db.Column(db.Boolean, default=False)
    foodType = db.Column(db.String(100))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'count': self.count,
            'point': self.point,
            'showAlternative': self.showAlternative,
            'foodType': self.foodType
        }
