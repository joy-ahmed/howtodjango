from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from blogs.models import *



def landing_page(request):
    return render(request, 'landing.html')


def create_user(request):
    if request.user.is_authenticated:
        return redirect('view_profile')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'create_user.html', {'form': form})



def update_user(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.user != user:
        return HttpResponse('Access denied')
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES ,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'user profile updated successfully')
            return redirect('view_profile')
        
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, 'update_user.html', {'form': form})


def login_page(request):
    if request.method == "POST":
        form = CustomLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful 🚀")
            return redirect('view_profile')
    else:
        form = CustomLoginForm()
    return render(request, 'login_page.html', {"form": form})



def logout_page(request):
    logout(request)
    messages.success(request, "You have been logged out 🏃‍♂️")
    return redirect('login')


@login_required
def view_profile(request):
    user = request.user
    user_posts = BlogPost.objects.filter(author=user).order_by('-created_at')
    return render(request, 'view_profile.html', {'user': user, 'posts': user_posts})


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('view_profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Manually add Bootstrap form-control class to each form field
        for field_name, field in context['form'].fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        return context
    
@login_required
def password_change(request):
    return CustomPasswordChangeView.as_view()(request)


@login_required
def password_change_done(request):
    return render(request, 'password_change_done.html')



