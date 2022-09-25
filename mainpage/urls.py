from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('', views.index, name='new_task'),
    path('categories/<int:category_id>/', views.show_category, name='category')
]
