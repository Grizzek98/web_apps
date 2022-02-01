from django.shortcuts import render

from startle_dreams.forms import PostForm
from startle_dreams.models import Post


def startle_dreams_index(request):
    posts = Post.objects.all().order_by('-title')
    context = {"posts": posts}
    return render(request, "startle_dreams_index.html", context)

def startle_dreams_form(request):
    form = PostForm(None)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                title = form.cleaned_data["title"],
                body = form.cleaned_data["body"],
            )
            post.save()

    context = {"form": form}
    return render(request, "startle_dreams_form.html", context)