from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import ItemModel,UserModel,StoreModel


class ItemType(SQLAlchemyObjectType):
    class Meta:
        model = ItemModel
        interfaces = (relay.Node, )

class StoreType(SQLAlchemyObjectType):
    class Meta:
        model = StoreModel
        interfaces = (relay.Node, )

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )
