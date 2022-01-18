from django.urls import path

from team.views import TeamPage

urlpatterns = [
    path('team', TeamPage.as_view()),
]