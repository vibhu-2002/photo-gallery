from django.contrib import admin

# Register your models here.
from app1.models import categories, Photo

admin.site.register(categories)
admin.site.register(Photo)