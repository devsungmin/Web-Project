from django.shortcuts import render,redirect, get_object_or_404,Http404
from .forms import *
from django.utils import timezone
from board.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request,"post_list.html",{"posts":posts})

@login_required
def post_create(request):
    if request.method=="POST":
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            post.author=request.user
            post.save()
            return redirect('post_list')
    elif request.method=="GET":
        form = Postform()
        return render(request, "post_create.html",{"form":form})

@login_required
def post_detail(request,id):
    post = get_object_or_404(Post, pk=id)
    return render(request,"post_detail.html",{"post":post})

def post_update(request,id):
    if request.method == "GET":
        post = get_object_or_404(Post, pk=id)
        form = Postform(instance=post)
        return render(request, "post_update.html",{"form":form,"post":post})
    elif request.method == "POST":
        post = get_object_or_404(Post, pk=id)
        form = Postform(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect("post_detail",id)
    return Http404()

def post_delete(request,id):
    post = get_object_or_404(Post,pk=id)
    if post.author != request.user:
        return redirect("main")
    post.delete()
    return redirect("post_list")