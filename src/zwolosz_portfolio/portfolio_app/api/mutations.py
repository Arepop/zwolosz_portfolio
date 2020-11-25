import graphene
from django.core.exceptions import ObjectDoesNotExist
from graphql_relay import from_global_id

from ..models import Tile
from .types import TileType
from .tools import update_mutation

class CreateTile(graphene.relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        file_name = graphene.String()
        description = graphene.String()
        size_x = graphene.Int()
        size_y = graphene.Int()

    tile = graphene.Field(TileType)
    
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

class UpdateTile(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String()
        file_name = graphene.String()
        description = graphene.String()
        size_x = graphene.Int()
        size_y = graphene.Int()

    tile = graphene.Field(TileType)

    @classmethod
    def mutate_and_get_payload(
        cls, 
        root, 
        info,
        id, 
        **kwargs   
    ):
        tile = Tile.objects.get(pk=from_global_id(id)[1])
        update_mutation(tile, tile.__class__, kwargs)
        
        tile.save()
        return UpdateTile(tile=tile)

class DeleteTile(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)\

    success = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(
        cls, 
        root, 
        info,
        id, 
    ):
        try:
            Tile.objects.get(pk=from_global_id(id)[1]).delete()
            success = True
        except ObjectDoesNotExist:
            success = False
        return DeleteTile(success=success)