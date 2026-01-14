from feeds.models import Feed
from feeds.types import FeedId
from packages.framework.usecases import CacheUseCaseAdapter, UseCaseAdapter


class FeedUseCase(UseCaseAdapter[Feed, FeedId]):
    def __init__(self):
        super().__init__(Feed)

    def optimize(self):
        return self.objects.all()


class FeedCacheUseCase(CacheUseCaseAdapter):
    cache_prefix = "feeds"


feed_use_case = FeedUseCase()
feed_cache_use_case = FeedCacheUseCase()
