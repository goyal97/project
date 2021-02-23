from django.shortcuts import render, HttpResponse

from .models import Contact


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        dob = request.POST.get('dob', '')
        phone = request.POST.get('name', '')
        email = request.POST.get('name', '')
        if name and dob and phone and email:
            contact = Contact(name=name, dob=dob, phone=phone, email=email)
            contact.save()
        else:
            return HttpResponse("Enter all the details")
    return render(request, 'index.html')
