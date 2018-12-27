from django.conf.urls import url
from basicapp import views

urlpatterns = [
  url(r'^$', views.index, name='index_basic_app'),
  url('form/', views.form_name_view),
]