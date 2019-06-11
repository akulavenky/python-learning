from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PostModel
from .forms import PostModelForm

# Create your views here.

def post_model_create_view(request):
    #if request.method == "POST":
    #    print(request.POST)
    #    form = PostModelForm(request.POST)
    #    if form.is_valid():
    #        form.save(commit=False)
    #        print(form.cleaned_data)
    form = PostModelForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save() 
        messages.success(request, "Create a new blog post")
        context = {
            "form": PostModelForm()
        }
        #If you don't want to redirect the page after form creation comment the below line
        #return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
    template = "blog/create-view.html"
    return render(request, template, context)


def post_model_detail_view(request, id=None):
    #obj = PostModel.objects.get(id=1)
    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object": obj
    }
    template = "blog/detail-view.html"
    return render(request, template, context)

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
    
