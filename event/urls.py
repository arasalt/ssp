from django.conf.urls.defaults import *
from event.views import *
from django.conf import settings
urlpatterns = patterns('event.views',
    url(r'this_event/(\d+)/$', 'event_detail', name = 'event_detail'),
    url(r'create_event/$', 'event_create', name = 'event_create'),
    url(r'event/', 'events_list', name = 'events_list'),
    
    
    
)
