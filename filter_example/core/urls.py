from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ListMedicos

router = SimpleRouter()

#router.register('medicos', ListMedicos.as_view(), 'medicos')

urlpatterns = [
    path('', include(router.urls)),
    path('medicos/', ListMedicos.as_view(), name='medicos'),
]