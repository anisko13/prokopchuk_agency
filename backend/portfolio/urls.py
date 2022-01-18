from django.urls import path

from portfolio.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view()),
]