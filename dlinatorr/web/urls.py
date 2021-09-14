from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/<str:query>', views.search, name='search'),
    path('add/', views.add, name='add'),
    path('signin', views.signin, name='signin'),
    path('new_account', views.new_account, name='new_account'),
    path('signout', views.signout, name='signout')
]
