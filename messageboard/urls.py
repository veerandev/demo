'''
Created on Apr 06, 2016

@author: Hisham
'''
from django.conf.urls import patterns, url, include
from messageboard.api import MessageBoardResource


message_board_resource = MessageBoardResource()
urlpatterns = patterns('',
    url(r'^api/v1/', include(message_board_resource.urls)),  
);