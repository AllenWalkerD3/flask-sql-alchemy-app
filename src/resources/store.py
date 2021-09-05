from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.get_item_by_name(name)
        if store:
            return {"store": store.json()}
        return {"message": "Store not found"}, 404

    def post(self,name):
        if StoreModel.get_item_by_name(name):
            return {"message": f"A store with name '{name}' already exists. "}, 400
        try:
            store = StoreModel(name)
            store.save_to_db()
        except:
            return {"message": "An error occurred while creating the store."}, 500
        return {"store": StoreModel.get_item_by_name(name).json()}, 201

    def delete(self, name):
        store = StoreModel.get_item_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": "Store deleted"}


class StoreList(Resource):
    def get(self):
        # return {"stores": [item.json() for item in StoreModel.query.all()]}
        return {"stores": list(map(lambda x: x.json(), StoreModel.query.all()))}