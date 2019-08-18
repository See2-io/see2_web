from django.urls import path

from .views import (CrispyGeneralSettingsFormView,
                    )

urlpatterns = [
    path('', CrispyGeneralSettingsFormView.as_view(), name='settings'),
]