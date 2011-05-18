from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('reg.views',
    url(r'login/$', 'login', name = 'login'),
    url(r'logout/$', 'logout', name = 'logout'),
    url(r'register/', 'register', name = 'register'),
    url(r'profile_client/(\d+)/show/$', 'client_profile', name = 'client_profile'),
    url(r'avatar/$', 'avatar', name = 'avatar'),
    url(r'profile_edit/(\d+)$', 'profile_edit', name = 'p_edit'),
    url(r'cv/$', 'cv', name = 'cv'),
    url(r'members/$', 'members', name = 'members'),
    url(r'profile_client/(\d+)/$', 'withoutedit', name = 'withoutedit'),
)
