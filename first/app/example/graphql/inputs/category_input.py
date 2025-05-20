# inputs.py
import strawberry_django
from strawberry import auto
from inventory.models import Category
import strawberry

@strawberry.input
class DeleteCategoryInput:
    id: int

@strawberry_django.input(Category)
class CategoryInput:
    name: auto
    slug: auto
    is_active: auto
    level: auto
    parent_id: int | None = None