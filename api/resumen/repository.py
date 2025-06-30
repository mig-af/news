from api.resumen.model import Resumen 

from api.init import db


class ResumenRepository:
    
    def get_all(self):
        """
        Aca se devuelve los resumenes del dia actual, en caso que aun no existan esos
        resumenes en la db, se mostraran los resumenes de la fecha anterior mas cercana
        los resumenes de hacen a las 10am de cada dia, entonces si una persona accede antes de las 10
        no le aparecera una carita triste, solo le mostrara los resumenes del dia anterior
        """
        ultima_fecha = db.session.query(func.max(Resumen.fecha)).filter(Resumen.fecha <= func.current_date()).scalar()
        rsum = Resumen.query.filter(Resumen.fecha == ultima_fecha).all()
        return rsum




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