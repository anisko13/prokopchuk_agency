from django.views.generic import ListView

from team.models import Teammate


class TeamPage(ListView):
    template_name = 'team/team.html'
    queryset = Teammate.objects.all()
