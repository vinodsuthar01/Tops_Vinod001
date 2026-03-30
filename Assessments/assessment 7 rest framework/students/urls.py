from rest_framework.routers import DefaultRouter
from students.views import *

router = DefaultRouter()
router.register('students',StudentsViewSet)

urlpatterns = router.urls