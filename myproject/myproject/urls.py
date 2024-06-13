# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp.views import RegisterView, LoginView  # Corrected import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  # Assuming you have a urls.py in myapp
]
