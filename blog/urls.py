from django.urls import path
from . import views
urlpatterns = [
##    path('api/Labeling/', views.post_list, name='Labeling'),
    path('', views.post_list, name='Labeling'),
]
