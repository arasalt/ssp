from django.conf.urls.defaults import *
from django.conf import settings
from ssp.views import main_page
from django.contrib.auth.decorators import login_required

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ssp.views',
	url(r'about/','about_page',name='about_page'),
	url(r'graduated/','graduated',name='graduated'),
	url(r'^$','main_page',name='main_page'),
	url(r'account/',include("reg.urls")),
	url(r'discussion/',include("discussion.urls")),
	url(r'files/',include("files.urls")),
	url(r'events/',include("event.urls")),
	url(r'anketa/',include("anketa.urls")),
    # Example:
    # (r'^ssp/', include('ssp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True} ),
    )
