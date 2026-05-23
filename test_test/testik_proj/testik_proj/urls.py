from django.contrib import admin
from django.urls import path
from testik_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

    path('main/', views.main_page, name="main_page"),

    path('create_request/', views.create_request, name="create_request")
]
