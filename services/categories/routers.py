from categories.controllers import CategorySetController
from packages.framework.routers import auto_router

app_name = "categories"

router = auto_router(CategorySetController)

urlpatterns = router.urls
