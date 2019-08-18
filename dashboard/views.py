# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


# Main dashboard page.
class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
