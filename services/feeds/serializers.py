from feeds.models import Feed
from packages.kernel.adapters import ModelSerializerAdapter


class FeedSerializer(ModelSerializerAdapter):

    class Meta:
        model = Feed
        fields = "__all__"
