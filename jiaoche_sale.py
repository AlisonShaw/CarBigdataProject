from config import db



class JiaoSales(db.Model):
    __tablename__ = "jiaoche_sale"
    id = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(255))
    TwntyMay = db.Column(db.INTEGER)
    TwntyApril = db.Column(db.INTEGER)
    TwntyMarch = db.Column(db.INTEGER)
    TwntyFeb = db.Column(db.INTEGER)
    TwntyJan = db.Column(db.INTEGER)
    NinDec = db.Column(db.INTEGER)
    Twnty = db.Column(db.INTEGER)
    Nin = db.Column(db.INTEGER)
    Eight = db.Column(db.INTEGER)