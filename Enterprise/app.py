from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/database'
db = SQLAlchemy(app)

from immobile import views as ImmobileView
from agency import views as AgencyView

@app.route('/')
def index():
    return 'Hello World !?'
    #return app.send_static_file('index.html')

@app.route('/immobiles', methods=['GET'])
def immobile_list():
    return ImmobileView.get_list()

@app.route('/immobiles', methods=['POST'])
def create_immobile():
    return ImmobileView.post()

@app.route('/immobiles/<int:id>', methods=['GET'])
def immobile_id(id):
    return ImmobileView.get(id)

@app.route('/immobiles/<int:id>', methods=['PUT'])
def update_immobile(id):
    return ImmobileView.update(id)

@app.route('/immobiles/<int:id>', methods=['DELETE'])
def delete_immobile(id):
    return ImmobileView.delete(id)

@app.route('/agencies', methods=['GET'])
def agency_list():
    return AgencyView.get_list()

@app.route('/agencies/<int:id>/immobiles', methods=['GET'])
def get_agency_immobiles(id):
    return ImmobileView.get_list_by_agency(id)

@app.route('/agencies/<int:id>/immobiles/<int:immobile_id>', methods=['GET'])
def get_immobile_by_agency(id, immobile_id):
    return ImmobileView.get_immobile_by_agency(id, immobile_id)

@app.route('/agencies', methods=['POST'])
def create_agency():
    return AgencyView.post()

@app.route('/agencies/<int:id>', methods=['GET'])
def agency_id(id):
    return AgencyView.get(id)

@app.route('/agencies/<int:id>', methods=['PUT'])
def update_agency(id):
    return AgencyView.update(id)

@app.route('/agencies/<int:id>', methods=['DELETE'])
def delete_agency(id):
    return AgencyView.delete(id)

if __name__ == '__main__':
    app.run()
