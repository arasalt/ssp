from django.contrib import admin
from reg.models import Client
from files.models import UserFile
from anketa.models import Anketa
from discussion.models import *
admin.site.register(Client)
admin.site.register(Discussion)
admin.site.register(Comment)
admin.site.register(UserFile)
admin.site.register(Anketa)


