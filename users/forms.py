from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


# General Settings
class GeneralSettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name',]


class CrispyGeneralSettingsForm(GeneralSettingsForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'show_btc_price',
            Submit('submit', 'Save')
        )

    def save(self, commit=True):
        m = super(GeneralSettingsForm, self).save(commit=False)
        # do custom stuff

        if commit:
            m.save()
        return m


class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name',]


class CrispyExchangeSettingsForm(ProfileSettingsForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )

    def save(self, commit=True):
        m = super(ProfileSettingsForm, self).save(commit=False)
        # do custom stuff

        if commit:
            m.save()
        return m
