from .forms import registration, personal
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from django.core.urlresolvers import reverse


def index(request):
    return HttpResponse("hello"+str(request))

def form(request):
    if request.method == "POST":
        form1 = registration(data=request.POST)
        form2 = personal(data=request.POST)
        print(form)
        if form1.is_valid():
            form1.save()
            form2.save()
            # cust_name = request.POST.get('cust_name')
            # cust_id = request.POST.get('cust_id')
            # print(cust_name,cust_id,"\n")
            # cust_details(cust_name=cust_name,cust_id=cust_id).save()

        return HttpResponseRedirect(reverse("registration"))
    else:
        formdata= registration()
        formdata2= personal()
        print(formdata)
        con={"form":formdata,"form2":formdata2}
        print(formdata2)
        return HttpResponse(render(request,template_name="forms.html",context=con))
