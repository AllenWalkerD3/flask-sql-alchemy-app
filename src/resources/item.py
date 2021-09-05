
from flask import current_app
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank"
    )
    parser.add_argument(
        "store_id", type=int, required=True, help="Every item needs a store id."
    )
    @jwt_required()
    def get(self, name):
        item = ItemModel.get_item_by_name(name)
        if item:
            return {"item": item.json()}
        return {"message": "Item not found"}, 404

    def post(self, name):

        item = ItemModel.get_item_by_name(name)
        if item:
            return {"message": "A user with that item already exist"}, 400

        data = Item.parser.parse_args()
        try:
            new_item = ItemModel(name, data["price"], data["store_id"])
            new_item.save_to_db()
        except:
            return {"message": "An Error occurred inserting the item."}, 500
        return {"item": ItemModel.get_item_by_name(name).json()}, 201

    def put(self, name):

        item = ItemModel.get_item_by_name(name)

        data = Item.parser.parse_args()
        try:
            
            if not item:
                item = ItemModel(None, name, data["price"], data["store_id"])
                item.save_to_db()
            else:
                item.price = data["price"]
            item.save_to_db()
        except:
            return {"message": "An Error occurred."}, 500

        return {"item": ItemModel.get_item_by_name(name).json()}

    def delete(self, name):
        item = ItemModel.get_item_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": "Item deleted"}


class ItemList(Resource):

    def get(self):
        # return {"items": [item.json() for item in ItemModel.query.all()]}
        return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}
