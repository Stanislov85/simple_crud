from django.contrib import admin
from django.urls import path, include

# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`
from rest_framework.routers import DefaultRouter
from measurements.views import ProjectViewSet, MeasurementViewSet

router = DefaultRouter()
router.register('Project', ProjectViewSet)
router.register('Measurement', MeasurementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
