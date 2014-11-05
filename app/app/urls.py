from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from accounts.views import ProfileView, RemoveUploadView


urlpatterns = patterns('',
    url(r'^$', login_required(TemplateView.as_view(template_name='home.html')), name='home'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^profile/upload/$', 'accounts.views.upload_file', name='upload'),
    url(r'^profile/removefile/(?P<pk>\d+)/$', RemoveUploadView.as_view(), name='file_remove'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


