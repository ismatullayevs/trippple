from django.urls import path
from django.views.generic import TemplateView
from .views import TourDetailView


app_name = 'tours'
urlpatterns = [
    path('', TemplateView.as_view(template_name='tours/tour_list.html'), name='tour_list'),
    path('<int:pk>/', TourDetailView.as_view(), name='tour_detail'),
    path('packages/', TemplateView.as_view(template_name='tours/tour_packages.html'), name='tour_packages'),
]