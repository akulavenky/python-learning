from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import PostModel

# Create your views here.
def post_model_detail_view(request, id=None):
    #obj = PostModel.objects.get(id=1) 		# another way
    obj = get_object_or_404(PostModel, id=id)   # another way
    
    #try:
    #    obj = PostModel.objects.get(id=10)
    #except:
    #    raise Http404				#another way

    #qs = PostModel.objects.filter(id=10)
    #obj = None
    #if not qs.exists() and qs.count() !=1:
    #    raise Http404
    #else:
    #    obj = qs.first()

    context = {
        "object": obj,
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
    print(request.user)
    qs = PostModel.objects.all()
    context = {
        "object_list": qs
    }

    try:
        user_is_authenticated = request.user.is_authenticated()
    except TypeError:
        user_is_authenticated = request.user.is_authenticated

    if user_is_authenticated:
        template = "blog/list-view.html"
    else:
        template = "blog/list-view-public.html"
        #raise Http404
    
    return render(request, template, context)
