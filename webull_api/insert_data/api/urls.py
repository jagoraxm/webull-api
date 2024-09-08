from rest_framework.routers import DefaultRouter
from insert_data.api.views import CompanyViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet, basename='company')
urlpatterns = router.urls