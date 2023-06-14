from django.shortcuts import render, redirect, get_object_or_404
from .models import studeninfo


# Create your views here.
def index(request):
    return render(request, 'index.html')


def formEntry(request):
    return render(request, 'entryform.html')


def recordData(request):
    data = studeninfo.objects.all()[0:]
    msg = f'all saved record from system'
    row_count = len(data)
    context = {
        'msg': msg,
        'data': data,
        'trow': row_count
    }
    return render(request, 'records.html', context)


def saveData(request):
    if request.method == "POST":
        stuID = request.POST.get('stdID')

        if studeninfo.objects.filter(stu_id=stuID).exists():
            msg = f'{stuID} already in system'
            data = studeninfo.objects.all()[0:]
            row_count = len(data)
            context = {
                'msg': msg,
                'data': data,
                'trow': row_count
            }
            return render(request, 'records.html', context)
        else:
            stuID = request.POST.get('stdID')
            stdName = request.POST.get('stdName')
            stdDOB = request.POST.get('stdDOB')
            stdAdd = request.POST.get('stdAdd')
            stdPhone = request.POST.get('stdPhone')
            stdEmPhone = request.POST.get('stdEmPhone')
            stdClass = request.POST.get('stdClass')
            stdImg = request.FILES.get('stdImg')

            studeninfo.objects.create(stu_id=stuID, stu_name=stdName, stu_dob=stdDOB,
                                      stu_address=stdAdd, stu_phone=stdPhone, stu_em_phone=stdEmPhone, stu_class=stdClass, stu_img=stdImg)
            msg = f'{stuID}-{stdName} has been added in system'
            data = studeninfo.objects.all()[0:]
            row_count = len(data)
            context = {
                'msg': msg,
                'data': data,
                'trow': row_count
            }
            return render(request, 'records.html', context)


def userinfo(request, stdid):
    usr = studeninfo.objects.get(stu_id=stdid)
    return render(request, 'userinfo.html', {'usr': usr})


def userinfoedit(request, stdid):
    usr = studeninfo.objects.get(stu_id=stdid)
    return render(request, 'editform.html', {'usr': usr})


def update(request, stdid):
    obj = get_object_or_404(studeninfo, stu_id=stdid)
    obj.stu_name = request.POST.get('stdName')
    # stdDOB = request.POST.get('stdDOB')
    obj.stu_address = request.POST.get('stdAdd')
    obj.stu_phone = request.POST.get('stdPhone')
    obj.stu_em_phone = request.POST.get('stdEmPhone')
    obj.stu_class = request.POST.get('stdClass')
    obj.save()

    data = studeninfo.objects.all()[0:]
    msg = f'{stdid} has been updated'
    row_count = len(data)
    context = {
        'msg': msg,
        'data': data,
        'trow': row_count
    }
    return render(request, 'records.html', context)


def delete(request, stdid):
    studeninfo.objects.get(stu_id=stdid).delete()
    
    data = studeninfo.objects.all()[0:]
    msg = f'{stdid} has been deleted'
    row_count = len(data)
    context = {
        'msg': msg,
        'data': data,
        'trow': row_count
    }
    return render(request, 'records.html', context)