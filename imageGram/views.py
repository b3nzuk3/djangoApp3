from django.shortcuts import render,redirect
from .models import User,Image,Comment
from .forms import PostForm
from django.db.models import Q



def search(request):
    ctx={}
    users = Image.objects.all()
    using = User.objects.all()
    if request.method == 'GET':
        query = request.GET.get("search")
        query_set = users.filter(
            Q(website__icontains=query)
            )
        query_setter = using.filter(
            Q(username__icontains=query)
        )
        total = query_set.count()
        ctx.update({
            'total':total,
            'query':query,
            'users':query_set,
            'using':query_setter
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
    posts= Image.objects.all().order_by("-created")
    if request.method == 'POST':
        uform = PostForm(request.POST, request.FILES)
        if uform.is_valid():
            post=uform.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('image-home')
    else:
        uform = PostForm()
    return render(request, 'imageGram/image_upload.html',{'uform': uform,'posts':posts})
