from django.contrib import admin
from django.urls import path
from astrology import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sign/', views.sign_view, name='sign'),
    path('house/', views.house, name='house'),
    path('planet/', views.planet, name='planet'),
    path('chart/', views.birth_chart_view, name='chart'),
    path('generate_chart/', views.generate_chart, name='generate_chart'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
