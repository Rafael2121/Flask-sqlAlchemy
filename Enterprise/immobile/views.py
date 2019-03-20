from app import db
from flask import jsonify, request
from immobile.models import Immobile

def get_list(page=1):
    immobiles = Immobile.query.paginate(page, 10).items
    list_immobiles = []
    for immobile in immobiles:
        list_immobiles.append(immobile_to_dict(immobile))
    return jsonify(list_immobiles)

def immobile_to_dict(immobile):
    return {
        "id": immobile.id,
	    "name": immobile.name,
	    "location": immobile.location,
	    "description": immobile.description,
	    "status" : immobile.status,
	    "type": immobile.type,
	    "goal": immobile.goal,
	    "agency_id": immobile.agency_id
    }

def get(id):
    immobile = Immobile.query.filter_by(id=id).first_or_404()
    return jsonify(immobile_to_dict(immobile))

def get_list_by_agency(id):
    immobiles = Immobile.query.filter_by(agency_id=id).all()
    list_immobiles = []
    for immobile in immobiles:
        list_immobiles.append(immobile_to_dict(immobile))
    return jsonify(list_immobiles)

def get_immobile_by_agency(id, immobile_id):
    immobile = Immobile.query.filter_by(agency_id=id, id=immobile_id).first_or_404()
    return jsonify(immobile_to_dict(immobile))

def post():
    name = request.json['name']
    location = request.json['location']
    description = request.json['description']
    status = request.json['status']
    type = request.json['type']
    goal = request.json['goal']
    agency = request.json['agency_id']
    new_immobile = Immobile(name, location, description, status, type, goal, agency)
    db.session.add(new_immobile)
    db.session.commit()
    return jsonify(immobile_to_dict(new_immobile))

def update(id):
    immobile = Immobile.query.filter_by(id=id).first_or_404()
    immobile.name = request.json['name']
    immobile.location = request.json['location']
    immobile.description = request.json['description']
    immobile.status = request.json['status']
    immobile.type = request.json['type']
    immobile.goal = request.json['goal']
    immobile.agency = request.json['agency_id']
    db.session.commit()
    return jsonify(immobile_to_dict(immobile))

def delete(id):
    immobile = Immobile.query.filter_by(id=id).first_or_404()
    db.session.delete(immobile)
    db.session.commit()
    return jsonify({})