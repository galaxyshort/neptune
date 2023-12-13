from django import forms
from persons.models import Person, Course


material_choices = [
    ('Debit Note Book', 'Debit Note Book'),
    ('Pen', 'Pen'),
    ('Exam Papers', 'Exam Papers'),
]

class PersonForm(forms.ModelForm):

    materials = forms.MultipleChoiceField(choices=material_choices, widget=forms.CheckboxSelectMultiple())

    def save(self):
        pass

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
