from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm




def post_list(request):
    posts = Post.objects.filter(data__lte=timezone.now()).order_by('data') 
    return render(request, 'ticket/post_list.html', {'posts': posts})

def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.data = timezone.now()
             post.save()
             return redirect('/admin', pk=post.pk)
     else:
         form = PostForm()
     return render(request, 'ticket/post_edit.html', {'form': form})
