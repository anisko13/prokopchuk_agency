from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import FAQView, PricingView, ServicesView, SeoserviceView, ReklamaView, ContactsView, WebsiteCreationView, SeoacademyView, SeokursobuchenieView, SmmprodvijenieView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('', include('team.urls')),
    path('faq', FAQView.as_view(), name='faq'),
    path('price', PricingView.as_view(), name='price'),
    path('services', ServicesView.as_view(), name='services'),
    path('seo-service', SeoserviceView.as_view(), name='seo-service'),
    path('reklama', ReklamaView.as_view(), name='reklama'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('website-creation', WebsiteCreationView.as_view(), name='website-creation'),
    path('seo-academy', SeoacademyView.as_view(), name='seo-academy'),
    path('seo-kurs-obuchenie', SeokursobuchenieView.as_view(), name='seo-kurs-obuchenie'),
    path('smm-prodvijenie', SmmprodvijenieView.as_view(), name='smm-prodvijenie'),

    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

