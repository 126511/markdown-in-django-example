from django.shortcuts import render
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import File

# Create your views here.
def index(request):
    files = File.objects.all()
    return render(request, "files/index.html", {
        "files" : files
    })

def add_file(request):
    if request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        print(f"submitting {title} and {body}")
        File(title=title, body=body).save()

        return HttpResponseRedirect(reverse(index))
    else:
        return render(request, "files/add_file.html")

def view_file(request, id):
    try:
        file = File.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse(index))
    
    return render(request, "files/view_file.html", {
        "file" : file
    })

def edit_file(request, id):
    try:
        file = File.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse(index))
    
    if request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        file.title = title
        file.body = body
        file.save()
        return HttpResponseRedirect(reverse(index))
   
    return render(request, "files/edit_file.html", {
        "file" : file
    })