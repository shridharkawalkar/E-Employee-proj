# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from dashboard.forms import EmployeeForm
from dashboard.models import Employee
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.functions import Lower


# Create your views here.
def index(request):
    order_by = request.GET.get('order_by','pk')
    records = Employee.objects.all().order_by(Lower(order_by))
    paginator = Paginator(records, 1)
    page = request.GET.get('page')
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
        
    success_message=None
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Form saved successfully"
    else:
        form = EmployeeForm()
    return TemplateResponse(request,"index.html",{"form":form, "success_message":success_message, "records":records})