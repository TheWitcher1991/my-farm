from calculators.controllers import CalculatorSetController
from packages.framework.routers import auto_router

app_name = "calculators"

router = auto_router(CalculatorSetController)

urlpatterns = router.urls
