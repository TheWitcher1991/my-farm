from diseases.controllers import DiseaseSetController
from packages.framework.routers import auto_router

app_name = "diseases"

router = auto_router(DiseaseSetController)

urlpatterns = router.urls
