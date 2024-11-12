from django import forms
from teste.models import usuarios, tarefas

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = '__all__'

class TarefaForm(forms.ModelForm):
    class Meta:
        model = tarefas
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['your_field_name'].queryset = tarefas.objects.all()  # Example queryset for a specific field