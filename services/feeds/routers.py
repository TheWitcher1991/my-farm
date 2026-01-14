from feeds.controllers import FeedSetController
from packages.framework.routers import auto_router

app_name = "feeds"

router = auto_router(FeedSetController)

urlpatterns = router.urls
