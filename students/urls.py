from django.urls import path

from students import views

urlpatterns = [ 
    path('catalog/', views.Catalog.as_view())
]