from django.urls import path
from .views import home, expanded_blog

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:post_id>/', expanded_blog, name='expanded_blog'),
]
