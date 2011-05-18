from django.conf.urls.defaults import *
from discussion.views import *
from django.conf import settings
urlpatterns = patterns('discussion.views',
    url(r'dis_create/', 'create_dis', name = 'create_dis'),
    url(r'dis_detail/(\d+)/show$', 'dis_detail', name = 'dis_detail'),
    url(r'dis_list/$', 'dis_list', name = 'dis_list'),
    url(r'HOME/$', 'home_profile', name = 'home_profile'),
    
)
