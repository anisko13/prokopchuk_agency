from django.views.generic import TemplateView

from main.models import ServiceFooter


class FAQView(TemplateView):
    template_name = 'main/faq.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='faq')
        return data


class PricingView(TemplateView):
    template_name = 'main/price.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='price')
        return data


class ServicesView(TemplateView):
    template_name = 'main/services.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='services')
        return data


class SeoserviceView(TemplateView):
    template_name = 'main/seo-service.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='seo-service')
        return data

class EventsView(TemplateView):
    template_name = 'main/events.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='events')

class ReklamaView(TemplateView):
    template_name = 'main/reklama.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='reklama')
        return data

class OrmmarketingView(TemplateView):
    template_name = 'main/orm-marketing.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='orm-marketing')
        return data

class ContactsView(TemplateView):
    template_name = 'main/contacts.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='contacts')
        return data


class WebsiteCreationView(TemplateView):
    template_name = 'main/website-creation.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='website-creation')
        return data


class SeoacademyView(TemplateView):
    template_name = 'main/seo-academy.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='seo-academy')
        return data


class SeokursobuchenieView(TemplateView):
    template_name = 'main/seo-kurs-obuchenie.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='seo-kurs-obuchenie')
        return data

class SmmprodvijenieView(TemplateView):
    template_name = 'main/smm-prodvijenie.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='smm-prodvijenie')
        return data