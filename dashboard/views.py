# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from dashboard.forms import EmployeeForm
from dashboard.models import Employee
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.functions import Lower


# Create your views here.
def index(request, emp_id =None):
    order_by = request.GET.get('order_by','pk')
    records = Employee.objects.all().order_by(Lower(order_by))
    paginator = Paginator(records, 10)
    page = request.GET.get('page')
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
        
    success_message=None
    if request.method =="POST":
        if not emp_id:
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                success_message = "Form saved successfully"
        else:
            form = EmployeeForm(request.POST, instance=Employee.objects.get(pk=int(emp_id)))
            form.save()
            success_message = "Form edit successfully"
    else:
        if not emp_id:
            form = EmployeeForm()
        else:
            form = EmployeeForm(instance= Employee.objects.get(pk=emp_id))
    return TemplateResponse(request,"index.html",{"form":form, "success_message":success_message, "records":records})