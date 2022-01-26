from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import FAQView, PricingView, ServicesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('', include('team.urls')),
    path('faq', FAQView.as_view(), name='faq'),
    path('price', PricingView.as_view(), name='price'),
    path('services', ServicesView.as_view(), name='services'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

