from rest_framework.routers import DefaultRouter
from .views import CitasViewSet

router = DefaultRouter()
router.register('citas', CitasViewSet)

urlpatterns = router.urls