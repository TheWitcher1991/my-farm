from articles.controllers import ArticleSetController
from packages.framework.routers import auto_router

app_name = "articles"

router = auto_router(ArticleSetController)

urlpatterns = router.urls
