from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os, datetime
from flask_cors import CORS 
from flask_jwt_extended import JWTManager

app = Flask(__name__)

DOMAIN = os.environ.get("DOMAIN")
SECRET_JWT = os.environ.get("SECRET_JWT")
DB_INFO = os.environ.get("DATABASE_INFO")

# Configuración de la base de datos existente
app.config['SQLALCHEMY_DATABASE_URI'] = DB_INFO
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# configuracion jwt
app.config["JWT_SECRET_KEY"] = SECRET_JWT
app.config["JWT_ACCES_TOKEN_EXPIRES"] = datetime.timedelta(days=365)


#cors
CORS(app, resources={
    # r"/api/*": {
    #     "origins": DOMAIN,
    #     "methods": ["POST"],
    #     "allow_headers": ["Authorization", "Content-Type"]
    # },
    r"/api/*":{
        "origins":"*",
        "methods":["GET", "POST"],

    }
})


# Inicializar extensiones
db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)