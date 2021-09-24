from flask import Flask, current_app
from flask_graphql import GraphQLView
from flask_jwt import JWT
from flask_restful import Api

from database import db
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister
from src.schema import schema
from security import authenticate, identity

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "secret_key"
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, "/register")


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
