from django.shortcuts import render

# Create your views here.
from app1.models import categories, Photo


def gallery_page_fn(request):
    category=request.GET.get('category')
    if category == None:
        data2=Photo.objects.all()
    else:
        data2=Photo.objects.filter(category__name=category)

    data1=categories.objects.all()
    dict1={
        'key1':data1,
        'key2':data2
    }
    return render(request,'gallerypage.html',dict1)

def photoinput_page_fn(request):
    data3=categories.objects.all()
    if request.method == "POST":
        data=request.POST
        image=request.FILES.get('image')
        if data['category']!='none':
            category=categories.objects.get(id=data['category'])
        elif data['new_category']!="":
            category,created=categories.objects.get_or_create(name=data['new_category'])
        else:
            category=None
        photo=Photo.objects.create(category=category,description=data['description'],Image=image)
    dict2={
        'key3':data3
    }
    return render(request,'photoinput.html',dict2)

def photoview_page_fn(request,pk):
    data4=Photo.objects.get(id=pk)
    dict3={
        'key4':data4
    }
    return render(request,'photoview.html',dict3)