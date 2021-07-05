from django.shortcuts import render, redirect
import uuid
from django.http import HttpResponse
from .models import Url
# Create your views here.

def index(request):
  return render(request, "index.html")


def create(request):
  if request.method == 'POST':
    url = request.POST['link']
    uid = str(uuid.uuid4())[:5]
    new_url = Url(link=url, uuid=uid)
    new_url.save()
  
  return render(request, "index.html", {"uid": uid})

def go(request, pk):
  url_details = Url.objects.get(uuid=pk)
  print(f"url_details: {url_details}")
  return redirect(url_details.link)