from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CausaViewSet, DonacionViewSet, api_total_donaciones, api_resumen_donaciones, UsuarioViewSet, CategoriaViewSet, ComentarioViewSet

router = DefaultRouter()
router.register('causas', CausaViewSet)
router.register('donaciones', DonacionViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('categorias', CategoriaViewSet)
router.register('comentarios', ComentarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/total_donaciones/', api_total_donaciones, name='total_donaciones'),
    path('api/resumen/', api_resumen_donaciones, name='api_resumen'),
]



urlpatterns += router.urls