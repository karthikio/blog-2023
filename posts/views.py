from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required


from .models import Post, Tag, Feedback
from .forms import postForm, FeedbackForm


@login_required
def postListView(request): 
  feeds = Feedback.objects.all()

  posts = Post.objects.all().order_by('-id')
  tags = Tag.objects.all()
  featured = Post.objects.filter(featured=True).latest('id')
  print(featured)
  context = {
    'posts': posts,
    'tags': tags,
    'featured': featured,
    'feeds': feeds
  }
  return render(request, 'posts/home.html', context)

@login_required
def postsDetailView(request, slug=None): 
  if slug is not None:
    try: 
      post = Post.objects.get(slug=slug)
    except Post.DoesNotExist: 
      raise Http404

  context = {
    'post': post,
  }
  return render(request, 'posts/post.html', context)


@login_required
def postCreateView(request):
  form = postForm()
  user = request.user
  if user.is_authenticated:
    if request.method == 'POST':
      form = postForm(request.POST, request.FILES)
      if form.is_valid():
        form.save(commit=False)
        form.instance.author = user
        form.save()
        return  redirect('/')
    else:
      form = postForm()
  context = {
    'form': form,
  }
  return render(request, 'posts/create.html', context)


@login_required
def postDeleteView(request, slug):
  user = request.user
  post = Post.objects.get(slug=slug)
  if post.author == user:
    if request.method == 'POST':
      post.delete()
      return redirect('/')
  context = {
    'post': post,
  }
  return render(request, 'posts/delete.html', context)


@login_required
def postEditView(request, slug):
  user = request.user
  post = Post.objects.get(slug=slug)
  if user == post.author:
    form = postForm(instance=post)
    if request.method == 'POST':
      form = postForm(request.POST, request.FILES ,instance=post)
      if form.is_valid():
        form.save()
        return redirect('post_detail_page', post.slug)
    else: 
      form = postForm(instance=post)

  context = {
    'form': form,
  }
  return render(request, 'posts/edit.html', context)

@login_required
def postSearchView(request):
  if request.method == 'GET':
    search = request.GET.get('search')
    print(search)
    if search != None:
      qs = Post.objects.filter(title__contains=search)
    else: 
      qs = ['']
    context = {'qs': qs, 'search': search,}
  return render(request, 'posts/search.html', context)


@login_required
def feedbackPage(request):
  user = request.user
  form = FeedbackForm()
  if user.is_authenticated:
    if request.method == 'POST':
      form = FeedbackForm(request.POST)
      if form.is_valid():
        form.save(commit=False)
        form.instance.author = user
        form.save()
        return  redirect('/')

  context = {
    'form': form, 
  }

  return render(request, 'posts/feedback.html', context)
