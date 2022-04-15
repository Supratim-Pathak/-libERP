
from django.http import HttpResponse
from django.shortcuts import redirect, render
from adminPannel.models import  books_info,stu_info

import adminPannel

# Create your views here.
def dashboard(request):
    return render(request, "adminPannel/dashboard.html")

def tableVw(request):
    book_No = books_info.objects.all()
    return render(request, "adminPannel/table.html", {'book' : book_No})

def formLoad(request):
    return render(request, 'adminPannel/forms.html')
     
def formSave(request):
    if request.method == 'POST':
        name = request.POST.get('stu_name')
        roll = request.POST.get('roll_no')
        sv = stu_info(stu_name=name, stu_roll = roll)
        if sv.save():
            msg = "<h1>Data inserted</h1>"
        return redirect('form')

