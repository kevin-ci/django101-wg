from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def view_all_blogs(request):
    all_blogs = BlogPost.objects.all()
    context = { "blogs": all_blogs }
    return render(request, 'diary/index.html', context)

def create_blog(request):
    if request.method == "POST":
        blog_form = BlogPostForm(request.POST)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('index')
            
    elif request.method == "GET":
        form = BlogPostForm()
        context = { "form": form }
        return render(request, 'diary/create-blog.html', context)