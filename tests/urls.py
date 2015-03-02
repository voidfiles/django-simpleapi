from django.conf.urls import patterns, url, include

from . import views
from simpleapi import simple_api_patterns

urlpatterns = patterns(
    '',
    url(r'^test1$', views.resp_test),
    url(r'^test2$', views.resp_test2),
    url(r'^test3$', views.resp_test3),
    url(r'^empty_response_test$', views.empty_response_test),
    url(r'^docstring_test$', views.docstring_test),
    url(r'^api/v1/', include(simple_api_patterns)),
)
