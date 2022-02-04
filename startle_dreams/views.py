from django.shortcuts import render

from startle_dreams.forms import PostForm
from startle_dreams.models import Post

# these views create the webpage using the respective templates
# when a request is sent by the user via their browser


def startle_dreams_index(request):
    # retrieve posts from database
    posts = Post.objects.all().order_by('-title') 
    context = {"posts": posts}
    return render(request, "startle_dreams_index.html", context) 

def startle_dreams_form(request):
    form = PostForm(None)
    if request.method == 'POST':
        form = PostForm(request.POST)
        # if the form is valid, create a new post object and save it in the database
        if form.is_valid():
            post = Post(
                title = form.cleaned_data["title"],
                body = form.cleaned_data["body"],
            )
            post.save()
            form = PostForm()

    context = {"form": form}
    # render the webpage using the template and the context
    return render(request, "startle_dreams_form.html", context)