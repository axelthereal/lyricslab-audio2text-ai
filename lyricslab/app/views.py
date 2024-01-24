from django.shortcuts import render 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Media
def home_view(req):
    ctx = {
        "view_name": "Home"
    }
    return render(req, 'pages/home.html', ctx)
 

# handles_forms_uploads
def upload_media(req):
    if req.method == 'POST' and req.FILES['fileObj']:
        fileObj = req.FILES['fileObj']
        filetitle = req.FILES['fileTitle']
        instance = Media(title=filetitle, media_file=fileObj)
        instance.save()
        return JsonResponse({
        "status": "success",
        "msg": "File Uploaded Successfully"
    })

    return JsonResponse({
        "status": "error",
        "msg": "File Not Found"
    }) 

    