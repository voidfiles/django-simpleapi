from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^test1$', views.resp_test),
    url(r'^test2$', views.resp_test2),
    url(r'^test3$', views.resp_test3),
)
