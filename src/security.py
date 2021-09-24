from resources.user import UserModel
from werkzeug.security import safe_str_cmp
from models import UserModel

def authenticate(username:str, password:str):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)