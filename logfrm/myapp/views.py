from django.shortcuts import render
from myapp.forms import UserForm, UserProFo

# Create your views here.

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'myapp/index.html')

@login_required
def special(request):
    return HttpsResponse('You are loggedIn, Great!')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProFo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'pro_pic' in request.FILES:
                profile.pr_p = request.FILES['pro_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProFo()
    return render (request, 'myapp/registration.html', {'userr_form':user_form, 'pro_form':profile_form, 're':registered})


def user_login(request):

  if request.method =='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpsResponse('Account Not Active')

    else:
        print("some one failed")
        print("usn:{} and pword:{}".format(username, password))
        return("invalid login details supplied")

  else:
    return render (request, 'myapp/login.html', {})
