from django.urls import path
from django.views.generic import TemplateView


app_name = 'tours'
urlpatterns = [
    path('', TemplateView.as_view(template_name='tours/tour_list.html'), name='tour_list'),
    path('packages/', TemplateView.as_view(template_name='tours/tour_packages.html'), name='tour_packages'),
    path('<int:pk>/', TemplateView.as_view(template_name='tours/tour_detail.html'), name='tour_detail'),
]