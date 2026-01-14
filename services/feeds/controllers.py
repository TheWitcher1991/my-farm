from feeds.filters import FeedFilter
from feeds.serializers import FeedSerializer
from feeds.usecases import FeedUseCase, feed_cache_use_case, feed_use_case
from packages.framework.controllers import ModelSetBaseSetController
from packages.usecases.serializer import SerializerUseCase
from users.permissions import IsAdminOrReadOnly


class FeedSetController(ModelSetBaseSetController):
    prefix = "feeds"
    tag_cache = feed_cache_use_case.cache_prefix

    use_case = FeedUseCase()
    serializer_use_case = SerializerUseCase()

    permission_classes = (IsAdminOrReadOnly,)

    queryset = feed_use_case.optimize()
    serializer_class = FeedSerializer
    filterset_class = FeedFilter
