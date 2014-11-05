from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from accounts.views import ProfileView


urlpatterns = patterns('',
    url(r'^$', login_required(TemplateView.as_view(template_name='home.html')), name='home'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
