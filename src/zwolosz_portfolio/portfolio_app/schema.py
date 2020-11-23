from graphene_federation import build_schema

from .api.schema import APIQuery, APIMutation

class Query(APIQuery):
    pass


class Mutation(APIMutation):
    pass


schema = build_schema(query=Query, mutation=Mutation)
