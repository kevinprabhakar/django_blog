from django.conf.urls import patterns, url
from f1 import views


urlpatterns=patterns('',
                     #These just link to the specific views
                     url(r'^$', views.index, name='index'),
                     url(r'^about/', views.about, name='about'),
                     url(r'^forms_practice', views.form_practice, name='forms practice'),
                     url(r'^contact_form', views.contact, name='contact form')
                     )

