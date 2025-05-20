# types.py
import strawberry_django
from strawberry import auto
from inventory.models import Category
import strawberry

@strawberry.type
class DeleteStatus:
    success: bool
    message: str

@strawberry_django.type(Category)
class CategoryType:
    id: auto
    name: auto
    slug: auto
    is_active: auto
    level: auto