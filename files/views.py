from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from reg.models import *


from django.conf import settings

from files.models import *
from files.forms import *
def upload(request,template_name="files/upload.html"):
    file = UserFile(user = request.user)
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES, instance = file)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('file_list'))
    else:
        form = UploadForm()
    c = RequestContext(request, {'form' : form })
    return render_to_response(template_name, c)
    
def file_list(request,template_name="files/file_list.html"):
    l = UserFile.objects.all()
    c = RequestContext(request, {'list' : l })
    return render_to_response(template_name, c)
