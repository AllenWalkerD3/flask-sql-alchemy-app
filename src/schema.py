import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .model_type import ItemType, StoreType, UserType


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    items = SQLAlchemyConnectionField(ItemType.connection)
    stores = SQLAlchemyConnectionField(StoreType.connection)
    users = SQLAlchemyConnectionField(UserType.connection)

schema = graphene.Schema(query=Query)
