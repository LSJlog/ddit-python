from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from HELLO_DJANGO.dao_emp import DaoEmp


def index(request):
    return HttpResponse("Hello, World")

def param(request):
    menu = request.GET.get("menu", '탕수육')
    return HttpResponse("param : {}".format(menu))

@csrf_exempt
def post(request):
    menu = request.POST.get("menu", "")
    # menu = request.POST['menu']
    return HttpResponse("post : {}".format(menu))

def forw(request):
    a = " 홍길동"
    b = ["손흥민", "이강인", "김민재"]
    c = [
        {'e_id' :'1', 'e_name' :'1', 'sex' :'1','addr':'1'},
        {'e_id' :'2', 'e_name' :'2', 'sex' :'2','addr':'2'},
        {'e_id' :'3', 'e_name' :'3', 'sex' :'3','addr':'3'}
    ]
    
    return render(request, "forw.html", {'a' : a, 'b' : b, 'c' : c})

def emp(request):
    de = DaoEmp()
    list = de.selectList()
    return render(request, "emp.html", {'list' : list})