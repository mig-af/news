
from api.init import db
import datetime

class Resumen(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    cuerpo = db.Column("cuerpo", db.String(1000), nullable=False)
    url = db.Column("url", db.String(200))
    fecha = db.Column("fecha", db.DateTime())


    def __init__(self, resumen):
        self.cuerpo = resumen["cuerpo"]
        self.url = resumen["url"]
        #self.fecha = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
        self.fecha = datetime.date.today()

        

    def __repr__(self):
        return {"id":self.id, "cuerpo":self.cuerpo, "url":self.url}

    def serialize(self):
        return {
            "id": self.id,
            "cuerpo": self.cuerpo,
            "url":self.url
        }
    def __str__(self):
        return self.cuerpo


