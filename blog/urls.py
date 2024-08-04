from django.urls import path
from django.views.generic import TemplateView


app_name = 'blog'
urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/blog_list.html'), name='blog_list'),
    path('<int:post_id>/', TemplateView.as_view(template_name='blog/blog_detail.html'), name='blog_detail'),
]