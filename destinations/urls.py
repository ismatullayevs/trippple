from django.urls import path
from django.views.generic import TemplateView


app_name = 'destinations'
urlpatterns = [
    path('', TemplateView.as_view(template_name='destinations/destination_list.html'), name='destination_list'),
    path('<int:pk>/', TemplateView.as_view(template_name='destinations/destination_detail.html'), name='destination_detail'),
]