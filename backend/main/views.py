from django.views.generic import TemplateView


class FAQView(TemplateView):
    template_name = 'main/faq.html'


class PricingView(TemplateView):
    template_name = 'main/price.html'

class ServicesView(TemplateView):
    template_name = 'main/services.html'
