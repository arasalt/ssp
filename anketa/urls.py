from django.conf.urls.defaults import *
from django.conf import settings
from anketa.views import *
urlpatterns = patterns('anketa.views',

    url(r'^$','anketa',name='anketa'),
    url(r'^message/$','message',name='message'),
)
