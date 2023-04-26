from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def student(request):
    SFO=StudentForms()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForms(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('data is not valid')

    return render(request,'student.html',d)
