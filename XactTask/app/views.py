"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest,JsonResponse, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import Variable, BooleanValue, StringValue
import time

def home(request):
    if request.POST:
        variable_name = request.POST['variable_name']
        variable_type = request.POST['variable_type']
        variable_value = request.POST['variable_value']
        print(variable_name,variable_type,variable_value)
        v = Variable(name=variable_name,type=variable_type,value=variable_value)
        v.save()
        print('Data Save Successfully!')
        if variable_value.lower().__contains__('true') or variable_value.lower().__contains__('false'):
            if bool(variable_value):
                b = BooleanValue(Value=variable_value,variable=v)
                print('Boolean Save Successfully')
        else:
            s = StringValue(Value=variable_value,variable=v)
            print('string Save Successfully')
        pass
        return render(request,'app/index.html',{'title':'Home Page','Message':'Data Save Successfully'})
    else:
        return render(request,'app/index.html',{'title':'Home Page'})
    pass