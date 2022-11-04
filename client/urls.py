from django.urls import path

from .views import TashqiMijozCreateApi, IchkiMijozCreateApi

urlpatterns = [
    path('external-client-create', TashqiMijozCreateApi.as_view(), name='external-client-create'),
    path('internal-client-create', IchkiMijozCreateApi.as_view(), name='internal-client-create')
]