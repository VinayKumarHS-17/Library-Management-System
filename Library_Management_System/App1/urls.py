from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("addbook/",views.addbook,name='addbook'),
    path("readbook/",views.readbook,name='readbook'),
    path("about/",views.about,name='about'),
    path("issuebook/<int:id>",views.issuebook,name='issuebook'),
    path("delete/<int:id>",views.delete,name='delete'),
    path("list/",views.list,name='list'),
]