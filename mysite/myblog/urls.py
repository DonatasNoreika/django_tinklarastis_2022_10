from django.urls import path
from .views import IrasasListView

urlpatterns = [
    path('irasai', IrasasListView.as_view(), name='irasai'),
]