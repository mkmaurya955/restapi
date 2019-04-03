from django.shortcuts import render
from django.http import HttpResponse
import json


def emp_view(request):
    emp_data={
    'eno':100,
    'ename':'Murali',
    'esal':'10000',
    'eaddr':'uttarpradesh'
    }
    resp='<h1>Employee number:{}<br> Employee Name:{} <br>Employee Salary:{} <br>Employee Address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

#sending response from cmd line for json using module httpie,curls
def emp_jsonview(request):
    emp_data={
    'eno':100,
    'ename':'Murali',
    'esal':'10000',
    'eaddr':'uttarpradesh'
    }
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data, content_type="application/json")#multipurpose internet mail extension(MIME)

#By using JsonResponse we directly use dict data
from django.http import JsonResponse
def emp_jsonview2(request):
    emp_data={
    'eno':100,
    'ename':'Murali',
    'esal':'10000',
    'eaddr':'uttarpradesh'
    }
    return JsonResponse(emp_data)


#Class Based views for json
from django.views.generic import View
from djangoapp.mixin import HttpResponseMixin
class jsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is the GET method'})
        #return HttpResponse(json_data,content_type='application/json')
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is the POST method'})
        #return HttpResponse(json_data,content_type='application/json')
        return self.render_to_http_response(json_data)

    def put(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is the PUT method'})
        #return HttpResponse(json_data,content_type='application/json')
        return self.render_to_http_response(json_data)

    def delete(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is the DELETE method'})
        #return HttpResponse(json_data,content_type='application/json')
        return self.render_to_http_response(json_data)
