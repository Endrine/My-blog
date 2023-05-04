from django.urls import path
from . import views

urlpatterns = [
    path("" , views.starting_page, name="starting-page"),
    path("posts", views.posts, name= "posts-page"),
    path("posts/<slug>", views.post_detail, name="post-detail-page") #/posts/my-first-post prej myfirstpost is a slug qe tani te views thirret si argument??  In Django, <slug> is a placeholder used in URL patterns to capture a portion of a URL and pass it as a parameter to a view function
]

