from documents.controllers import DocumentSetController
from packages.framework.routers import auto_router

app_name = "documents"

router = auto_router(DocumentSetController)

urlpatterns = router.urls
