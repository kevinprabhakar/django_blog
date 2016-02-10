from django.conf.urls import patterns, url
from blogsite import views

urlpatterns = patterns('',
                       url(r'^$',views.home,name='home'),
                       url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
                       url(r'^create_post', views.create_post, name='create_post'),
                       url(r'^register', views.register, name='register'),
                       url(r'^login', views.auth_login,name='login'),
                       url(r'^logout', views.logout, name='logout'),
                      )