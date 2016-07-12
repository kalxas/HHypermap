from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from hypermap.api import views

urlpatterns = [
    url(r'^search/$', views.Search.as_view()),
    url(r'^docs/$', TemplateView.as_view(template_name='api/swagger/index.html')),
]

urlpatterns = format_suffix_patterns(urlpatterns)