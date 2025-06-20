from api.init import app, api
from api.controller import resumenController   


# Enlace de ruta al recurso

api.add_resource(resumenController.ResumenController, "/api", "/api/<string:data>")

app = app
if __name__ == '__main__':
    
    app.run(debug=True)
