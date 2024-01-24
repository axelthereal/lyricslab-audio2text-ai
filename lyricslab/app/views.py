from django.shortcuts import render 
from django.http import JsonResponse
from .models import Media
def home_view(req):
    ctx = {
        "view_name": "Home"
    }
    return render(req, 'pages/home.html', ctx)
 

# handles_forms_uploads
def upload_media(req):
    if req.method == 'POST' and req.FILES['fileObj']:
      try:
        fileObj = req.FILES["fileObj"]
        filetitle = req.POST.get("fileTitle")
        dbreq = Media(title=filetitle, media_file=fileObj)
        dbreq.save()
      except Exception as ex:
        logger.exception("An error occurred while handling the file upload")
        return JsonResponse({'status': 'error'})

    return JsonResponse({
        "status": "success",
        "msg": "File Uploaded Successfully"
    })

    return JsonResponse({
        "status": "error",
        "msg": "File Not Found"
    }) 

    