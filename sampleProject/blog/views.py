from django.shortcuts import render

# Create your views here.
from blog.models import Post

# model manager
# object

def blog_list(request):
    post = Post.objects.all() # select * from post
    front_end_ma_pathaune_data = {'post_table_ko_data': post, 'test_value':1}
    return render(request, 'list.html', context=front_end_ma_pathaune_data)

def blog_detail(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'details.html', context={})