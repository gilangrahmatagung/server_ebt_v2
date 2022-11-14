from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import func

from config import config, env

SERVER_PORT = env.int("SERVER_PORT")

app = Flask(__name__)
app.config.from_object(config[env.str("ENV")])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Data(db.Model):
    __tablename__ = 'tb_data'

    data_id = db.Column(db.Integer, primary_key=True)
    raspi_id = db.Column(db.Integer, nullable=False)
    source = db.Column(db.String(50))
    sensor = db.Column(db.String(50))
    current = db.Column(db.Float)
    voltage = db.Column(db.Float)
    power = db.Column(db.Float)
    api_created_at = db.Column(db.DateTime)
    db_created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())

    def __init__(self, raspi_id, source, sensor, current, voltage, power, api_created_at):
        self.raspi_id = raspi_id
        self.source = source
        self.sensor = sensor
        self.current = current
        self.voltage = voltage
        self.power = power
        self.api_created_at = api_created_at

    def __repr__(self):
        return '<data_id {}>'.format(self.data_id)

class DataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Data

def format_response(data, message="success"):
    return jsonify({"message": message, "data": data, })

@app.route('/akuisisi/sensor', methods=["GET", "POST"])
def sensor_get_and_create():
    if request.method == "GET":
        serializer = DataSchema(many=True)
        data = Data.query.all()
        return format_response(serializer.dump(data)), 200

    elif request.method == "POST":
        raspi_id = request.json.get("raspi_id")
        source = request.json.get("source")
        sensor = request.json.get("sensor")
        current = request.json.get("current")
        voltage = request.json.get("voltage")
        power = request.json.get("power")
        api_created_at = request.json.get("api_created_at")

        serializer = DataSchema()
        data = Data(
            raspi_id=raspi_id, 
            sensor=sensor, 
            source=source, 
            current=current, 
            voltage=voltage, 
            power=power, 
            api_created_at=api_created_at
            )

        db.session.add(data)
        db.session.commit()

        return format_response(serializer.dump(data)), 201


if __name__ == "__main__":
    app.run(port=SERVER_PORT)
