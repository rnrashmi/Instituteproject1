from django.shortcuts import render
from django.http.response import HttpResponse
from Institute.models import StudentInfo,FeedbackData


import datetime as dt
date1=dt.datetime.now()


def index(request):
    return render(request,'staticfile.html')
def home_view(request):
    return render(request,'inhe_home.html')

def contact_view(request):
    if request.method=="POST":
        sname=request.POST.get('sname')
        smobile=request.POST.get('smobile')
        scourse=request.POST.get('scourse')
        sloc=request.POST.get('sloc')

        data=StudentInfo(
            sname=sname,
            smobile=smobile,
            scourse=scourse,
            sloc=sloc
        )

        data.save()

        return render(request, 'inhe_contact.html')

    else:
        return render(request, 'inhe_contact.html')


def Retrieve_view(request):
    dat=StudentInfo.objects.all()
    return render(request,'inhe_services.html',{'dat':dat})


def services_view(request):
    return render(request,'inhe_services.html')

def gallery_view(request):
    return render(request,'inhe_gallery.html')


def feedback_view(request):
    if request.method == "POST":
        name1=request.POST.get('name')
        rating1=request.POST.get('rating')
        feedback1=request.POST.get('feedback')

        data=FeedbackData(
            name=name1,
            rating=rating1,
            date=date1,
            feedback=feedback1
        )

        data.save()
        newfeedback = FeedbackData.objects.all()
        return  render(request,'feedbackview.html',{'newfeedback':newfeedback})

    else:
        newfeedback=FeedbackData.objects.all()
        return render(request,'feedbackview.html',{'newfeedback':newfeedback})









