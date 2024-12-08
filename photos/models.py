from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name="category name" , null=False , blank=False)
    def __str__(self):
        return self.name
    
class Photo(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(null=False,blank=False)
    description=models.TextField(verbose_name="description")
    
    def __str__(self):
        return self.description