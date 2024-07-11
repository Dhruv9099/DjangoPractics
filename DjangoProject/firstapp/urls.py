from django.urls import path
from . import views

urlpatterns = [
    path('',views.firstapp,name='firstapp'),
    path('<int:script_id>/', views.detail, name='detail'),
] 