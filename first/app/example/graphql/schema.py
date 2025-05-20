# schema.py

import strawberry
from example.graphql.mutations.mutation import Mutation


@strawberry.type
class Query:
    # Temporary placeholder field
    hello: str = "Hello world"


schema = strawberry.Schema(query=Query, mutation=Mutation)
