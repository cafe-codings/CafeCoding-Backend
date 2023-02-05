from django.urls import path

from . import views

app_name = 'cafe_list'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:cafe_list_id>/', views.detail, name='detail'), #cafe_info_id 이게 불안
]