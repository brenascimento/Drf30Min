# URLs do Projeto
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import ClienteViewSet

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
