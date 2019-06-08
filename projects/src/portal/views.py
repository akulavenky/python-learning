from django.http import HttpResponse

def home(request):
    #return HttpResponse("<h1>Hello World</h1>")
    response = HttpResponse()
    response.write("Here is the hello world")
    return response
