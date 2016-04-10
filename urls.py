from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'views.home', name='home'),
    url(r'^', include('messageboard.urls')),

)
