from django.conf.urls import patterns, url
from website import views

urlpatterns = [
                   url(r'^$',views.register,name='register'),
                   url(r'^login', views.auth_login, name='login'),
                   url(r'^home', views.home, name='home'),
                   url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
                   url(r'^logout', views.logout, name='logout'),
                   url(r'^create_post', views.create_post, name='create_post'),
                ]
