from django.contrib.auth.models import User
from django import forms
from user_form.models import Form, Skills


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class UserForm2(forms.ModelForm):

    class Meta:
        model = Form
        fields = ['category', 'skills', 'income', 'edu_qualification']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['skills'].queryset = Skills.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['skills'].queryset = Skills.objects.filter(category_id = category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['skills'].queryset = self.instance.category.skills_set.order_by('name')