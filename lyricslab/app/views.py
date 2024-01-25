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
    if req.method == 'POST' and req.FILES.get('fileObj'):
      try:
        fileObj = req.FILES.get('fileObj')
        filetitle = req.POST.get("fileTitle")
        uploadreq = Media.objects.create(title=filetitle,  media_file=fileObj)
        uploadreq.save()
      except Exception as ex:
        print(f"Error : {ex}") 
        return JsonResponse({'status': 'error'})

    return JsonResponse({
        "status": "success",
        "msg": "File Uploaded Successfully"
    })

  
    