from django.urls import path
from django.views.generic import TemplateView


app_name = 'hotels'
urlpatterns = [
    path('', TemplateView.as_view(template_name='hotels/hotel_list.html'), name='hotel_list'),
    path('<int:pk>/', TemplateView.as_view(template_name='hotels/hotel_detail.html'), name='hotel_detail'),
]