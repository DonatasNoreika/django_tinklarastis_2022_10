from django.urls import path
from .views import (IrasasListView,
                    IrasasDetailView,
                    IrasasCreateView,
                    IrasasUpdateView,
                    IrasasDeleteView)

urlpatterns = [
    path('irasai/', IrasasListView.as_view(), name='irasai'),
    path('irasai/<int:pk>/', IrasasDetailView.as_view(), name='irasas'),
    path('irasai/naujas', IrasasCreateView.as_view(), name='irasas_naujas'),
    path('irasai/<int:pk>/redaguoti', IrasasUpdateView.as_view(), name="irasas_update"),
    path('irasai/<int:pk>/trinti', IrasasDeleteView.as_view(), name="irasas_delete")
]