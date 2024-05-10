from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError(_("Le mot de passe doit être composé d'au moins 8 caractères."))
        return password1

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Les deux mots de passe ne sont pas identiques"))
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class EmailForm(forms.Form):
    from_email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"placeholder": _("Adresse email")}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"placeholder": _("Sujet")}))
    body = forms.CharField(max_length=600, widget=forms.Textarea(attrs={"placeholder": _("Message")}))

    def send_email(self):
        EmailMessage(
            subject=self.cleaned_data["subject"],
            body=self.cleaned_data["body"],
            from_email=self.cleaned_data["from_email"],
            to=[settings.TO_EMAIL]
        ).send()
