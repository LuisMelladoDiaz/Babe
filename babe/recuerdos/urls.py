from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('coleccion', views.RecuerdoListView.as_view(), name='lista_recuerdos'),
    path('nuevo/', views.crear_recuerdo, name='crear_recuerdo'),
    path('<int:pk>/editar/', views.editar_recuerdo, name='editar_recuerdo'),
    path('<int:pk>/eliminar/', views.RecuerdoDeleteView.as_view(), name='eliminar_recuerdo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

