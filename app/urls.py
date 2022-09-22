
from django.urls import path
from .views import Home, PostDetails, post_tags, custom_login, signup, custom_logout, add_blog, custom_search


urlpatterns = [
    path('', Home, name='home'),   
    path('add_blog/', add_blog, name='add_blog'),
    path('login/', custom_login, name='login'),   
    path('signup/', signup, name='signup'),
    path('logout/', custom_logout, name='logout'),
    path('<slug:slug>/', PostDetails, name='post_detail'),
    path('tag/<str:name>/', post_tags, name='post_tags'),
    path(r'^search/$', custom_search, name='search'),
      
]