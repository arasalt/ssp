from django.conf.urls.defaults import *
from django.conf import settings
from anketa.views import *
urlpatterns = patterns('anketa.views',

    url(r'^$','anketa',name='anketa'),
    url(r'^message/$','message',name='message'),
    url(r'^anketa_list/$','anketa_list',name='anketa_list'),
    url(r'^anketa_detail/(\d+)/$','anketa_detail',name='anketa_detail'),
    url(r'^invite/anketa_number/(\d+)/$','invite',name='invite'),
    
)
