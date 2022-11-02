from . import views
from django.urls import path

app_name = 'clientTumi'

urlpatterns = [
    path('',views.index,name='index'),
    path('subirArchivos',views.subirArchivos,name='subirArchivos'),
    path('descargarArchivos',views.descargarArchivos,name='descargarArchivos'),
    path('descargarImagen/<str:ind>',views.descargarImagen,name='descargarImagen'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('consultarRequest',views.consultarRequest,name='consultarRequest'),
]