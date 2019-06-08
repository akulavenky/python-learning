from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import PostModel


# Create your views here.

def post_model_list_view(request):
    qs = PostModel.objects.all()
    context = {
        "object_list": qs
    }
    template = "blog/list-view.html"
    return render(request, template, context)

@login_required(login_url='/login/')
def login_required_view(request):
    #qs = PostModel.objects.all()
    #print(qs)
    #return HttpResponse("Some data") 
   
    #template rendering
    #print(request.user)
    qs = PostModel.objects.all()
    template = "blog/list-view.html"
    context = {
        "object_list": qs
    }

    return render(request, template, context)

    #try:
    #    user_is_authenticated = request.user.is_authenticated()
    #except TypeError:
    #    user_is_authenticated = request.user.is_authenticated

    #if user_is_authenticated:
    #    template = "blog/list-view.html"
    #else:
    #    template = "blog/public-list-view.html"


    #if user_is_authenticated:
    #    template = "blog/list-view.html"
    #else:
    #    template = "blog/public-list-view.html"
    #    raise Http404 
    
