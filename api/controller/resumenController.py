from flask_restful import Resource, reqparse
from api.resumen.repository import ResumenRepository
import json
from api.resumen.model import Resumen
from api.user.model import User 
from api.security.jwt import jwt_req





repository = ResumenRepository()
parser = reqparse.RequestParser()
parser.add_argument('status', required=True, help='El campo status es obligatorio', type=bool)
parser.add_argument('data', required=True, help='El campo data es obligatorio', type=dict)



class ResumenController(Resource):


    def get(self, data=None):

        
        
        if(data != None):
            resp = repository.find_by_date(date=data)
            
            if(resp):
                print(type(resp))
                return [{"id":i.id, "cuerpo":i.cuerpo, "url":i.url} for i in resp], 200
            else:
                return {"Data":"No hay datos"}, 404




        print("get iniciado")
        data = repository.get_all()


        if(data):
            return [{"id":i.id, "cuerpo":i.cuerpo, "url":i.url} for i in data], 200
        else:
            return {"Data":"No hay datos"}, 404
        
    
    @jwt_req()
    def post(self, data = None):
        data = parser.parse_args()
        
        print(type(data))
        ia_resumen = data
        try:
            
            print(type(ia_resumen["status"]))
            resumenes = []
            if(ia_resumen["status"] == True):
                for i in ia_resumen["data"]["resumen"]:
                    datos = {"cuerpo":i[0], "url":i[1][0]}
                    resumenes.append(Resumen(datos))

                for resumen in resumenes:
                    print(type(resumen))
                    print(resumen.url)
                    repository.save(resumen)
                #print(data)
                return data, 201
            else:
                return data, 400
        except Exception as e:

            return data, 400

    @jwt_req()
    def delete(self, data:int):
        
        if(Resumen.query.get(data)):

            dlt = repository.delete(data)
            print(dlt)
            print(data)
            return {}, 204
        else:
            return "Not found", 404


    