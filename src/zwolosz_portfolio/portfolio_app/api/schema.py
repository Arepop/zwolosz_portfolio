from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .types import TileType
from .mutations import CreateTile

class APIQuery(ObjectType):
    tile = relay.Node.Field(TileType)
    all_tiles = DjangoFilterConnectionField(TileType)

class APIMutation(ObjectType):
    create_tile = CreateTile.Field()
