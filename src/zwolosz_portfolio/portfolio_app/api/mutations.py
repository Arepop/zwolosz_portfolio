from django.db.models.lookups import GreaterThan
import graphene
from .types import TileType
from ..models import Tile



class CreateTile(graphene.relay.ClientIDMutation):
    tile = graphene.Field(TileType)

    class Input:
        name = graphene.String(required=True)
        file_name = graphene.String()
        description = graphene.String()
        size_x = graphene.Int()
        size_y = graphene.Int()

    @classmethod
    def mutate_and_get_payload(
        cls, 
        root, 
        info, 
        name,
        file_name,
        description,
        size_x,
        size_y,
    ):
        tile = Tile.objects.create(
        name=name,
        file_name=file_name,
        description=description,
        size_x=size_x,
        size_y=size_y,
        )
        tile.save()
        return CreateTile(tile=tile)