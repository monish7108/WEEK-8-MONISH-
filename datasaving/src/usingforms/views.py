# from django.http import HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from django.shortcuts import render
# from .forms import register2, personal2
# # from .models import customer_details,personaldetails
#
# def index(request):
#     return HttpResponse("hello")
#
# def form(request):
#     if request.method == "POST":
#         form1 = register2(request.POST)
#         form2 = personal2(request.POST)
#         # print(form1.fields)
#         # print(form)
#         # if form1.is_valid():
#         form1.save()
#         form2.save()
#             # form1.cleaned_data['first_name']
#             # personaldetails(first_name=form1.cleaned_data['first_name']).save()
#             # cust_name = request.POST.get('cust_name')
#             # cust_id = request.POST.get('cust_id')
#             # print(cust_name,cust_id,"\n")
#             # customer_details(cust_name=cust_name,cust_id=cust_id).save()
#
#         return HttpResponseRedirect(reverse("register"))
#     # else:
#     if request.method == "GET":
#         formdata= register2()
#         formdata2 = personal2()
#         print(formdata)
#         con={"form1":formdata,"form2":formdata2}
#         print(formdata2)
#         return render(request,"forms.html",con)
#



from .forms import register2, personal2
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from django.core.urlresolvers import reverse


def index(request):
    return HttpResponse("hello")

def form(request):
    if request.method == "POST":
        form1 = register2(data=request.POST)
        form2 = personal2(data=request.POST)
        print(form)
        if form2.is_valid() and form1.is_valid():
            # form1.save()
            print(form1.cleaned_data)
            print(form2.cleaned_data)
            # form2.save()
            # cust_name = request.POST.get('cust_name')
            # cust_id = request.POST.get('cust_id')
            # print(cust_name,cust_id,"\n")
            # cust_details(cust_name=cust_name,cust_id=cust_id).save()

        return HttpResponseRedirect(reverse("register"))
    if request.method=="GET":
        formdata= register2()
        formdata2= personal2()
        print(formdata,"\n")
        con={"form2":formdata2,"form":formdata}
        print(formdata2,"\n")
        return HttpResponse(render(request,template_name="forms2.html",context=con))
