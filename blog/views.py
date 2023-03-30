from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import*

# Create your views here.

def HoemePage(request):
    header = BlogPost.objects.all()
    queryset = BlogPost.objects.filter(status = 'published').order_by('-created')
    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    template_name = 'blogs/index.html'
    context = {'posts':posts, 'header':header}
    return render(request, template_name, context)


def category(request):
    queryset = BlogPost.objects.filter(status = 'published').order_by('-created')
    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    template_name = 'blogs/category.html'
    context = {'posts':posts}
    return render(request, template_name, context)

def single_post(request, slug):
    queryset = BlogPost.objects.filter(status = 'published').order_by('-created')
    paginator = Paginator(queryset, 3)
    page_number = request.GET.get('page')
    recent_posts = paginator.get_page(page_number)

    post = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blogs/single.html'
    context = {'post':post, 'recent_posts':recent_posts}
    return render(request, template_name, context)





