from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, UpdateView
from django.urls import reverse_lazy
from .forms import (GeneralSettingsForm,
                    CrispyGeneralSettingsForm,
                    )
from .models import Profile


class GeneralSettingsFormView(LoginRequiredMixin, UpdateView):
    form_class = GeneralSettingsForm
    success_url = reverse_lazy('settings')
    template_name = 'account/settings.html'


class CrispyGeneralSettingsFormView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = CrispyGeneralSettingsForm
    success_url = reverse_lazy('settings')
    template_name = 'account/settings.html'

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super(CrispyGeneralSettingsFormView, self).get_context_data(**kwargs)
        if self.request.POST:
            pass
        else:
            pass
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.created_by = self.request.user
        # self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('settings',)
