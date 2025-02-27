from django.urls import path
from .views import home, expanded_blog, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:post_id>/', expanded_blog, name='expanded_blog'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
