from app import db
from agency.models import Agency
from flask import jsonify, request

def get_list(page=1):
    agencies = Agency.query.paginate(page, 10).items
    list_agencies = []
    for agency in agencies:
        list_agencies.append(agency_to_dict(agency))
    return jsonify(list_agencies)

def agency_to_dict(agency):
    return {
        'id': agency.id,
        'name' : agency.name,
        'location' : agency.location,
    }

def get(id):
    agency = Agency.query.filter_by(id=id).first_or_404()
    return jsonify(agency_to_dict(agency))

def post():
    data = request.json
    name = str(data['name'])
    location = str(data['location'])
    new_agency = Agency(name, location)
    db.session.add(new_agency)
    db.session.commit()
    return jsonify(agency_to_dict(new_agency))

def update(id):
    agency = Agency.query.filter_by(id=id).first_or_404()
    agency.name = request.json['name']
    agency.location = request.json['location']
    db.session.commit()
    return jsonify(agency_to_dict(agency))

def delete(id):
    agency = Agency.query.filter_by(id=id).first_or_404()
    db.session.delete(agency)
    db.session.commit()
    return jsonify({})

