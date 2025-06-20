from api.resumen.model import Resumen 

from api.init import db


class ResumenRepository:
    
    def get_all(self):
        return Resumen.query.all()




    def save(self, resumen:Resumen):
        
        db.session.add(resumen)
        db.session.commit()
        
        return 201

    def delete(self, id:int):
        resumen = Resumen.query.get(id)
        db.session.delete(resumen)
        db.session.commit()
        return 204

    def find_by_date(self, date):
        
        return Resumen.query.filter(Resumen.fecha == date).all()