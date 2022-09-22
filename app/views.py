
from django.shortcuts import render, redirect, HttpResponse, get_list_or_404
from .models import Card, Tag
from .forms import BlogForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from django.urls import reverse
# Create your views here.



def Home(request):   
    cards = Card.objects.all().filter(published=True).order_by('-publish_date')
    card_list = Tag.objects.all()
    tag_list = Tag.objects.filter(card__title__startswith='These')
    recent_post = Card.objects.all()[:4]
    p = Paginator(cards, 3) # returns how many pages to display
    
    page_number = request.GET.get('page')# returns the desired page object
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        # returns the desired page object
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {
        'count' : p.num_pages,
        'card' : page_obj,
        'card_list': card_list,
        'recent_post' : recent_post ,
        'tag_list':tag_list

    }
    return render(request, 'index.html', context)
    

def PostDetails(request, slug):
    post = Card.objects.filter(slug=slug)  
    recent_post = Card.objects.all()[:4]
    context = {
        'post': post, 
        'recent_post': recent_post
    }
    return render(request, 'details.html', context)

def post_tags(request,name):
    recent_post = Card.objects.all()[:4]   
    post_list = Tag.objects.get(name=name).card_set.all()
   
    context = {      
        'post_list':post_list,
        'recent_post':recent_post,

    }
    return render(request, 'tags.html', context)


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse('User is invalid')
        login(request, user)   
        return redirect('add_blog')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', { 'form': form })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():           
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', { 'form':form })

def custom_logout(request):
    logout(request)

    return redirect('home')

@login_required(login_url = '/login/') #if not logged in redirect to login url
def add_blog(request):
    
    if request.method == 'POST':  
        # create a form instance and populate it with data from the request:
        form  = BlogForm(request.POST, request.FILES or None) #request.FILES for upload content files

        # check whether it's valid:
        if form.is_valid():

            # Create new form object but don't save to database yet
            try:
                form.save()
            except:
                form.errors
            # Save the form to the database
                     
            return redirect('home') # redirect to a new URL:
        else:
            return form.errors

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BlogForm()    

    return render(request, 'add-blog.html', {'form':form})


def custom_search(request):
    query = request.GET.get('query', '') # second is default parameter which is empty, should add name="query" in search field
    cards = Card.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query))

    return render(request, 'search.html', {'cards':cards, 'query': query})