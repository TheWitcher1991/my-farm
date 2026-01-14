from feeds.models import Feed
from feeds.types import FeedId
from packages.framework.usecases import UseCaseAdapter


class FeedUseCase(UseCaseAdapter[Feed, FeedId]):
    def __init__(self):
        super().__init__(Feed)

    def optimize(self):
        return self.objects.all()


feed_use_case = FeedUseCase()
