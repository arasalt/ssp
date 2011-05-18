from django.db import models
from django.contrib.auth.models import User
from files.models import *

class UserFile(models.Model):
    def upload_to_dir(self, filename):
        return 'userdata/uploads/%s/%s' % (self.user.username, filename)
    user = models.ForeignKey(User)
    file = models.FileField(upload_to=upload_to_dir)
