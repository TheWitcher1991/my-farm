from categories.models import Category
from packages.kernel.adapters import FilterAdapter


class CategoryFilter(FilterAdapter):
    class Meta:
        model = Category
        fields = (
            "created_at",
            "updated_at",
        )
