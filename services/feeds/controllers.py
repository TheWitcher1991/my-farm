from feeds.serializers import FeedSerializer
from feeds.usecases import FeedUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class FeedSetController(BaseSetController):
    prefix = "feeds"

    use_case = FeedUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = FeedSerializer
