from django.conf.urls.defaults import *

urlpatterns = patterns('files.views',
    url(r'^list/$', 'file_list', name='file_list'),
    url(r'^upload/$', 'upload', name='upload_file'),
)
