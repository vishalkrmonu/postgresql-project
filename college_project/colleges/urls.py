# colleges/urls.py

from django.urls import path
from .views import home, add_college, update_college, delete_college

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_college, name='add_college'),
    path('update/<int:college_id>/', update_college, name='update_college'),
    path('delete/<int:college_id>/', delete_college, name='delete_college'),
]
