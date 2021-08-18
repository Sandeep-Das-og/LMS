from django.shortcuts import render

from django.views.generic import ListView
from students import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
# Create your views here.

class Catalog(LoginRequiredMixin, ListView):
    queryset = models.Course.objects.all()
    context_object_name = 'courses'
    template_name = 'students/catalog.html'
    login_url = '/auth/login'

    def get_queryset(self):
        return models.Course.objects.filter(
            Q(user = self.request.user.pk)
        )


#class Home(LoginRequiredMixin, ListView):
    #queryset = models.Course.objects.all()
    #context_object_name = 'courses'
    #template_name = 'students/home.html'
    #login_url = 'auth/login'

    #def get_queryset(self):
        #return models.Course.objects.filter(user = self.request.user)


def Courses(request):
    template_name = 'students/courses.html'
    return render(request, template_name)
    