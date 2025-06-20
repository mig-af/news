import jwt
import os
from api.user.model import User
from flask import request

SECRET_JWT_KEY = os.environ.get("SECRET_JWT_KEY")


def decode(jwt_token:str):
    try:
        jwt_token = jwt_token.replace("Bearer ", "")
        resp = jwt.decode(jwt_token, SECRET_JWT_KEY, algorithms="HS256")
        return True, resp 
    except Exception as e:
        return False, e
    

def verify_user(jwt_token):
    dat = decode(jwt_token)
    if(dat[0] == True):
        print(dat[0])
        try:
            user = User.query.filter(User.name == dat[1]["user"]).first()
            if(user.name):
                return True 

        except:
            return False

    else:
        return dat
    
def jwt_req():
    def req_auth(func):
        def wrapper(*args):
            resp = verify_user(request.headers.get("Authorization"))
            if( resp == True):
                return func(*args)
            else:
                print(resp)
                return {"msg":"Unauthorized"}, 401
        return wrapper
    return req_auth
