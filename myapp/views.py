from django.shortcuts import render,redirect
from django.http import HttpResponse
import uuid
from .models import URL
# Create your views here.

def shortly(request):
    if request.method=="POST":
        longURL=request.POST["link"]
        customText=request.POST.get("custom","")
        url_entry = URL.objects.filter(link=longURL).first()

        if(url_entry!=None):
            oldShortLink=str(url_entry.shortLink)
            ind=oldShortLink.find("-")
            if(ind==-1):
                if(customText!=''):
                 url_entry.shortLink= customText+"-"+url_entry.shortLink 
            else:
                if(customText==''):
                    url_entry.shortLink=oldShortLink[-5:]
                else:
                    url_entry.shortLink=customText+"-"+oldShortLink[-5:]
            url_entry.save()   
            return render(request,"shortly.html",{"link":longURL,"shortLink":url_entry.shortLink})
        else:
            shortURL=customText
            if(customText!=""):
                shortURL+="-"
            shortURL += str(uuid.uuid4())[-5:]
            newURL = URL(link=longURL, shortLink=shortURL)
            newURL.save()
            return render(request,"shortly.html",{"link":longURL,"shortLink":shortURL})

def go(request,pk):
    try:
        url_entry = URL.objects.get(shortLink=pk)
        return redirect(url_entry.link)
    except URL.DoesNotExist:
        return render(request,"notFound.html")
    
def index(request):
    return render(request,"index.html",{})
