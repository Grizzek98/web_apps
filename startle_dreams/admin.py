from django.contrib import admin
from startle_dreams.models import Post

# creates a listing to interact with the database
# via localhost:8000/admin URL

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)