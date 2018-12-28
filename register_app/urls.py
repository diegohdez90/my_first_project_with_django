from django.conf.urls import url
from register_app import views

app_name = 'register_app'

urlpatterns = [
  url(r'^$',views.index, name="register_index"),
  url('register/', views.register, name='register'),
  url('login/', views.user_login, name="user_login"),
]