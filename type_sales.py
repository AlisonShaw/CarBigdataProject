from config import db



class TypeSales(db.Model):
    __tablename__ = "type_sales"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255))
    TwntyMay = db.Column(db.INTEGER)
    TwntyAprail = db.Column(db.INTEGER)
    TwntyMarch = db.Column(db.INTEGER)
    TwntyFeb = db.Column(db.INTEGER)
    TwntyJan = db.Column(db.INTEGER)
    NinDec = db.Column(db.INTEGER)
    Twnty = db.Column(db.INTEGER)
    Nin = db.Column(db.INTEGER)
    Eight = db.Column(db.INTEGER)