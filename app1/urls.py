from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('user/', views.index, name='index'),
    path('recognize/', views.recognize, name='recognize'),
    path('afterCam/', views.afterCam, name = "afterCam")

    # #/music/
    # url(r'^$', views.index, name = 'index'),

    # #/music/71/
    # url(r'^(?P<album_id>)$'),
]