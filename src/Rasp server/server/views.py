from django.http import HttpResponse
import os

def take_photo(request):
    os.system("python control_script_version_2.py")
    return HttpResponse("Take Photo Successful.")