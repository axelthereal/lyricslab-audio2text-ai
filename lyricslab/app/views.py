from django.shortcuts import render
from django.http import HttpResponse

def home_view(req):
    ctx = {
        "view_name": "Home"
    }
    return render(req, 'pages/home.html', ctx)
 