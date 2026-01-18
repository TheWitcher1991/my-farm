from calculators.controllers import RationCalculationSetController, WeightCalculationSetController
from packages.framework.routers import auto_router

app_name = "calculators"

router = auto_router(RationCalculationSetController, WeightCalculationSetController)

urlpatterns = router.urls
