from .models import Form, Skills
from django import forms


class UserForm(forms.ModelForm):

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