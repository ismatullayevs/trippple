from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('home2/', TemplateView.as_view(template_name='index2.html'), name='index2'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    path('admin/', admin.site.urls),
    path('tours/', include('tours.urls')),
    path('hotels/', include('hotels.urls')),
    path('activities/', include('activities.urls')),
    path('blog/', include('blog.urls')),
    path('destinations/', include('destinations.urls')),
]
