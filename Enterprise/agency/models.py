from app import db

class Agency(db.Model):
    __tablename__ = 'Agency'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    location = db.Column(db.String(45), nullable=False)

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return '<Agency %d>' % self.id