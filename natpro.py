from config import db



class NatPro(db.Model):
    __tablename__ = "natpro"
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(255))
    yoy_growth = db.Column(db.String(255))