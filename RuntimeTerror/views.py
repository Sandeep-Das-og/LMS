from django.shortcuts import render

def index(request):
    template_name = 'main/home.html'
    return render(request, template_name)

def aboutUs(request):
    template_name = 'main/aboutus.html'
    return render(request, template_name)

def contactUs(request):
    template_name = 'main/contactus.html'
    return render(request, template_name)

def notFound(request):
    return render(request, 'main/site.html')