from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#login view
def loginView(request):
  form = AuthenticationForm()
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('/')
  else:
    form = AuthenticationForm()

  context = {
    'form': form,
  }

  return render(request, 'accounts/login.html', context)


#register view
def registerView(request):
  form = UserCreationForm()
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
  context = {
    'form': form,
  }

  return render(request, 'accounts/register.html', context)


#logout view
@login_required
def logoutView(request):
  logout(request)
  return redirect('login_page')