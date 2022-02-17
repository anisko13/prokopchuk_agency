from django.views.generic import ListView

from main.models import HeaderSlide, ServiceFooter
from portfolio.models import PortfolioProject


class IndexPage(ListView):
    template_name = 'portfolio/index.html'
    queryset = PortfolioProject.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['seo_texts'] = ServiceFooter.objects.filter(page__title='main')
        data['slides'] = HeaderSlide.objects.filter(is_active=True)

        return data
