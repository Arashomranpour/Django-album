from django.urls import path
from . import views

urlpatterns = [
    path("",views.gallery,name="gallery",),
    path("photo/<str:pk>",views.viewphoto,name="photo",),
    path("add/",views.addphoto,name="add",),
    path("delete/<str:pk>",views.DeletePhoto.as_view(),name="delete")
    
    
]
