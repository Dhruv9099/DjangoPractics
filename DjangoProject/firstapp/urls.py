from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/firstapp/
    path('',views.firstapp,name='firstapp'),
    path('order/',views.order,name="order"),
    path('detail/<int:script_id>/', views.detail, name='detail'),
    path('script-stores/', views.script_store_view, name='script_stores')
] 