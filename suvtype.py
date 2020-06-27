from config import db


class SuvType(db.Model):
    __tablename__ = "suvtype"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    lowPrice = db.Column(db.DECIMAL)
    highPrice = db.Column(db.DECIMAL)
    averPrice = db.Column(db.DECIMAL)
    comment = db.Column(db.DECIMAL)
