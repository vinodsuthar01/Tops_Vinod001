from rest_framework.routers import DefaultRouter
from enrolls.views import *

router = DefaultRouter()
router.register('enrolls',EnrollsViewSet)

urlpatterns = router.urls