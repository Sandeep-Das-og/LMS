
from django.contrib import admin
from django.urls import path, include
from RuntimeTerror import views
from students import views as studentViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('students/', include('students.urls')),
    path('courses/', studentViews.Courses),
    path('about/',views.aboutUs),
    path('contactus/',views.contactUs),
    path('site/', views.notFound),
    path('',views.index)
]
