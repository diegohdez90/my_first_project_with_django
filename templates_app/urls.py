from django.conf.urls import url
from templates_app import views

# template tagging

app_name = 'templates_app'

urlpatterns = [
  url(r'^$', views.index, name='index_templates'),
  url('other/', views.other, name='other'),
  url('relative/', views.relative, name='relative')
]