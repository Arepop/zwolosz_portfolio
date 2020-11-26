import graphene
from django.core.exceptions import ObjectDoesNotExist
from graphql_relay import from_global_id
from datetime import datetime
from django.utils import timezone

from ..models import Tile
from .types import TileType
from .tools import update_mutation

class CreateTile(graphene.relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        file_name = graphene.String(required=False)
        description = graphene.String(required=False)
        size_x = graphene.Int(required=False)
        size_y = graphene.Int(required=False)

    tile = graphene.Field(TileType)
    
    @classmethod
    def mutate_and_get_payload(
        cls, 
        root, 
        info, 
        name,
        **kwargs
    ):

        tile = Tile.objects.create(name=name)
        update_mutation(tile, tile.__class__, kwargs)
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
        tile.edited = datetime.now(tz=timezone.get_current_timezone())
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