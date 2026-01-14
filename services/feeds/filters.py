from feeds.models import Feed
from packages.kernel.adapters import FilterAdapter


class FeedFilter(FilterAdapter):
    class Meta:
        model = Feed
        fields = (
            "created_at",
            "updated_at",
        )
