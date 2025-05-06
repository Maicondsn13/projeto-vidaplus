from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PacienteViewSet, ProfissionalViewSet, UnidadeViewSet, ConsultaViewSet, ProntuarioViewSet
from .views import RegisterView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'profissionais', ProfissionalViewSet)
router.register(r'unidades', UnidadeViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'prontuarios', ProntuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

