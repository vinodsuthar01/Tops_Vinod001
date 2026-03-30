from rest_framework.routers import DefaultRouter
from courses.views import *

router = DefaultRouter()
router.register('courses',CoursesViewSet)

urlpatterns = router.urls