from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageForm
from django.db.models import Q



def search(request):
    ctx={}
    images = Image.objects.all()
    if request.method == 'GET':
        query = request.GET.get("search")
        query_set = images.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(location__name__icontains=query )
            )
        total = query_set.count()
        ctx.update({
            'total':total,
            'query':query,
            'images':query_set
        })

        return render(request, "imageGram/search.html", ctx)


def home(request):
    images=Image.objects.all()
    ctx = {'images': images}

    return render(request, 'imageGram/home.html', ctx)


def postImage(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        description = request.POST.get('description')
        new_post = Image.objects.create(user=request.user, image=image, description=description)
        new_post.save()
        return redirect('image-home')
    return render(request, 'imageGram/image_upload.html')
