from app import db

class Immobile(db.Model):
    __tablename__ = 'Immobile'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    location = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(45), nullable=False)
    status = db.Column(db.Boolean)
    type = db.Column(db.String(45), nullable=False)
    goal = db.Column(db.String(45), nullable=False)
    agency_id = db.Column(db.Integer, db.ForeignKey('Agency.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, name, location, description, status, type, goal, agency_id):
        self.name = name
        self.location = location
        self.description = description
        self.status = status
        self.type = type
        self.goal = goal
        self.agency_id = agency_id

    def __repr__(self):
        return '<Immobile %d>' % self.id