from django.views.generic import ListView

from portfolio.models import PortfolioProject


class IndexPage(ListView):
    template_name = 'portfolio/index.html'
    queryset = PortfolioProject.objects.all()
