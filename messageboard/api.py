'''
Created on Apr 06, 2016

@author: Hisham
'''
import json

from decimal import Decimal

from django.conf.urls import url
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.http import HttpResponse

from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash
from tastypie.validation import Validation

from messageboard.models import Message

'''
    Message Board APIs
'''

class MessageBoardResource(ModelResource):
    class Meta:
        queryset = Message.objects.all()
        allowed_methods = ['get', 'post', 'delete']
        resource_name = 'message'
        authorization = Authorization()
        always_return_data = True
        limit = 0
        max_limit = 0

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_all_or_create_resource'), name="get_all_or_create_resource_v1"),
            url(r"^(?P<resource_name>%s)/(?P<pk>\d+)%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_or_delete_resource'), name="get_or_delete_resource_v1"),
        ]

    def get_all_or_create_resource(self, request, **kwargs):
        self.method_check(request, allowed=['post', 'get'])
        if request.method == 'POST':        
            data = json.loads(request.body)
            user = data.get('user', '')
            content = data.get('content', '')
            success, response = Message.objects.add_message(user=user, content=content)
            if not success:
                data = serializers.serialize('json', [response])
                response = HttpResponse(data, mimetype='application/json')
                response.status_code = 400
                response.reason_phrase = "BAD REQUEST"
                return response
            else:  
                data = serializers.serialize('json', [response])
                response = HttpResponse(data, mimetype='application/json')
                response.status_code = 201
                response.reason_phrase = "CREATED"
                return response
        elif request.method == 'GET':
            response = Message.objects.all()
            data = serializers.serialize('json', response)
            response = HttpResponse(data, mimetype='application/json')
            response.status_code = 200
            response.reason_phrase = "OK"
            return response

    def get_or_delete_resource(self, request, **kwargs):
        self.method_check(request, allowed=['get', 'delete'])
        try:
            message = Message.objects.get(pk=kwargs['pk'])
            if request.method == 'GET':
                data = serializers.serialize('json', [message])
                response = HttpResponse(data, mimetype='application/json')
                response.status_code = 200
                response.reason_phrase = "OK"
                return response    
            elif request.method == 'DELETE':                
                message = Message.objects.get(pk=kwargs['pk'])
                message.delete()
                data = ''
                response = HttpResponse(data, mimetype='application/json')
                response.status_code = 204
                response.reason_phrase = "NO CONTENT"
                return response
        except ObjectDoesNotExist:
            data = ''
            response = HttpResponse(data, mimetype='application/json')
            response.status_code = 404
            response.reason_phrase = "NOT FOUND"
            return response