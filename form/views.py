from django.shortcuts import render, redirect
from .models import studeninfo


# Create your views here.
def index(request):
    return render(request, 'index.html')


def formEntry(request):
    return render(request, 'entryform.html')


def recordData(request):
    data = studeninfo.objects.all()[0:]
    msg = f'all saved record from system'
    content = {
        'msg': msg,
        'data': data
    }
    return render(request, 'records.html', content)


def saveData(request):
    if request.method == "POST":
        stuID = request.POST.get('stdID')

        if studeninfo.objects.filter(stu_id=stuID).exists():
            msg = f'{stuID} already in system'
            data = studeninfo.objects.all()[0:]
            content = {
                'msg': msg,
                'data': data
            }
            return render(request, 'records.html', content)
        else:
            stuID = request.POST.get('stdID')
            stdName = request.POST.get('stdName')
            stdDOB = request.POST.get('stdDOB')
            stdAdd = request.POST.get('stdAdd')
            stdPhone = request.POST.get('stdPhone')
            stdEmPhone = request.POST.get('stdEmPhone')
            stdClass = request.POST.get('stdClass')

            studeninfo.objects.create(stu_id=stuID, stu_name=stdName, stu_dob=stdDOB,
                                      stu_address=stdAdd, stu_phone=stdPhone, stu_em_phone=stdEmPhone, stu_class=stdClass)
            msg = f'{stuID}-{stdName} has been added in system'
            data = studeninfo.objects.all()[0:]
            content = {
                'msg': msg,
                'data': data
            }
            return render(request, 'records.html', content)
