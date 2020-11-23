import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from ..models import Tile


class TileType(DjangoObjectType):
    class Meta:
        model = Tile
        interfaces = (relay.Node,)
        filter_fields = ['name', 'created', 'edited']

        