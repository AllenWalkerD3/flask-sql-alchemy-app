import os
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from database import db
from src.resources.user import UserRegister
from src.resources.item import Item, ItemList
from src.resources.store import Store, StoreList 
from src.security import authenticate, identity

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///mydb.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "secret_key"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, "/register")


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
