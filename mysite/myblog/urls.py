from django.urls import path
from .views import (IrasasListView,
                    IrasasDetailView,
                    IrasasCreateView)

urlpatterns = [
    path('irasai/', IrasasListView.as_view(), name='irasai'),
    path('irasai/<int:pk>/', IrasasDetailView.as_view(), name='irasas'),
    path('irasai/naujas', IrasasCreateView.as_view(), name='irasas_naujas'),
]