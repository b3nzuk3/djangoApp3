from django.shortcuts import render,redirect
from .models import User,Image,Comment
from django.db.models import Q



def search(request):
    ctx={}
    users = User.objects.all()
    if request.method == 'GET':
        query = request.GET.get("search")
        query_set = users.filter(
            Q(username__icontains=query)
            )
        total = query_set.count()
        ctx.update({
            'total':total,
            'query':query,
            'users':query_set
        })

        return render(request, "imageGram/search.html", ctx)


def home(request):
    images=Image.objects.all()
    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            post = post,
            body = request.POST.get('body')
        )
        post.comments = post.comments + 1
        post.save()
        return redirect('post', pk=post.id)
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
