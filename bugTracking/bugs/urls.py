from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.login, name='login'),

    url(r'^login/$', views.login, name='login'),
    #url(r'^(?P<user_id>[0-9]+)/bugs/$', views.bug_list, name='bugs'),
    url(r'^bugs/$', views.bug_list, name='bugs'),    
    #url(r'^logged_in/$', views.logged_in, name='logged_in'),
    url(r'^newbug/$', views.new_bug, name='new_bug'),
]
