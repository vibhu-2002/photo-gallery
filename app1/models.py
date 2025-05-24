from django.db import models

# Create your models here.
class categories(models.Model):
    name=models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category=models.ForeignKey(categories,on_delete=models.SET_NULL,null=True)
    Image=models.ImageField(blank=False,null=False)
    description=models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return self.description
