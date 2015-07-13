from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.template.context_processors import csrf

from .models import Bug
from .form import AddBugForm 

'''
def login(request):
    template = loader.get_template('bugs/login.html')

    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))
'''
def login(request):
    if request.user and request.user.is_authenticated():
        return redirect('bugs')

    state = ""
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.user = user
                return redirect('bugs') 
                #return render_to_response('bugs/bug_list.html')
            else:
                print 'user is not active'
                state = "Your account have not actived"
        else:
            state = "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."
    c = {}
    c.update(csrf(request))
    c['username'] = username
    c['state'] = state
    return render_to_response('bugs/login.html', c)


'''
def logged_in(request):
    return render_to_response('logged_in.html', context_instance=RequestContext(request))
'''


def bug_list(request):
    bug_list = Bug.objects.all()
    template = loader.get_template('bugs/bug_list.html')
    context = RequestContext(request, {
        'bug_list': bug_list,
    })
    return HttpResponse(template.render(context))


def new_bug(request):
    form = AddBugForm()
    if request.POST:
        form = AddBugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.owner = request.user
            bug.save()
            return redirect('bugs')

    context = {
        'form': form
    }
    context.update(csrf(request))
    return render_to_response('bugs/new_bug.html', context)