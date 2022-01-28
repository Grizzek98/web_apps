from django.shortcuts import render

from startle_dreams.models import Post


def startle_dreams_index(request):
    posts = Post.objects.all().order_by('-title')
    context = {"posts": posts}
    return render(request, "startle_dreams_index.html", context)