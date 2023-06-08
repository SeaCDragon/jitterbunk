from django.urls import path

from . import views
app_name = "Bunks"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:from_user>', views.user, name='user'),
    path('new', views.new, name='new')
]