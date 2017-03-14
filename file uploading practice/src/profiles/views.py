from django.shortcuts import render, reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import registrationform
from .models import myprofile
# from django.views import generic

def index(request):
    return HttpResponse("HELLO!")

def registration(request):

    if request.method == "POST":
        formdata=registrationform(data=request.POST,files=request.FILES)
        print(request.POST)
        if formdata.is_valid():
            formdata.save()
            print("succeeded.")
        return HttpResponseRedirect(reverse("registration"))

    else:
        print("invalid form")
        formdata=registrationform()
        return render(request, "newprofile.html",{"form":formdata})

def myview(request):
    query_results = myprofile.objects.filter(first_name="Monish Lalchandani")
    con={"data":query_results}
    return render(request,"viewprofile.html",con)