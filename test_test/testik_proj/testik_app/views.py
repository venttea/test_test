from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils import timezone


def is_client(user):
    try:
        app_user = User.objects.get(login=user.username)
        return app_user.role.id == 4
    except User.DoesNotExist:
        return False

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main_page')
        return render (request, 'login.html')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def main_page(request):
    user = get_object_or_404(User, login=request.user.username)

    requests = Request.objects.filter(client=user).order_by('-start_date')

    return render(request, 'main_page.html', {
        'user_role': user.role_id,
        'requests': requests
    })

@login_required
def create_request(request):
    user = get_object_or_404(User, login=request.user.username)

    if user.role_id != 4:
        return redirect('access_denied')

    types = TechType.objects.all()

    if request.method == 'POST':
        tech_type_id=request.POST.get('tech_type')
        tech_model=request.POST.get('tech_model')
        description=request.POST.get('description')

        new_request = Request.objects.create(
            start_date=timezone.now().date(),
            tech_type_id=tech_type_id,
            tech_model=tech_model,
            description=description,
            status_id=3,
            client=user
        )

        return redirect('main_page')
    return render(request, 'create_request.html', {'types':types})