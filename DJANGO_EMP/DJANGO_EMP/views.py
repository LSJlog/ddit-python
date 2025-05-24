from django.http import request
from DJANGO_EMP.dao_emp import DaoEmp
from conda_build import render

def emp_list(request):
    de = DaoEmp()
    list = de.selectList()
    return render(request, "emp_list.html", {'list' : list})