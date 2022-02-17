from modeltranslation.translator import translator, TranslationOptions
from .models import PortfolioProject


class PortfolioProjectTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(PortfolioProject, PortfolioProjectTranslationOptions)
