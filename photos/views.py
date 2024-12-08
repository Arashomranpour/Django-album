from django.http import HttpResponse
from django.shortcuts import  render ,redirect
from .models import Category ,Photo
from .forms import photoform
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
import os
from django.conf import settings

# Create your views here.
def gallery(request):
    ca=request.GET.get("category")
    if ca==None:
        photo=Photo.objects.all()

    else:  
        photo=Photo.objects.filter(category__name=ca)

    cat=Category.objects.all()
    
    # photo=Photo.objects.all()
    if not photo.exists():  # `photo.exists()` is a more accurate way to check for an empty queryset
        images_dir = os.path.join(settings.BASE_DIR, 'static/images')

        # Ensure the directory exists before attempting to clear it
        if os.path.exists(images_dir):
            for filename in os.listdir(images_dir):
                file_path = os.path.join(images_dir, filename)

                # Remove files
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    # Optionally handle subdirectories (if any)
                    os.rmdir(file_path)
    context={"cat":cat,"photo":photo}
    return render(request,"photos/gallery.html",context=context)


def addphoto(request):
    cat=Category.objects.all()
    
    if request.method == "POST":
        data=request.POST
        image=request.FILES.getlist("images")
        if data["Category"] !="None":
            category=Category.objects.get(id=data["Category"])
        elif data["Category_new"] != "":
            category, created = Category.objects.get_or_create(name=data["Category_new"])
        else :
            category=None

        for imag in image:
            photo=Photo.objects.create(category=category,description=data["Description"],image=imag)
            
        
        return redirect("gallery")
        
    context={"cat":cat}
        
    return render(request,"photos/add.html",context=context)


def viewphoto(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,"photos/photo.html",context={"photo":photo})


class DeletePhoto(DeleteView):
    model = Photo
    success_url = reverse_lazy("gallery")
    template_name = "photos/delete.html"
    