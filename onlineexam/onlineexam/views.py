from django.shortcuts import render
from onlineexam.models import Exam



def examonline(request):
    results = Exam.objects.all()
    return render(request, 'Index.html', {"Exam": results})