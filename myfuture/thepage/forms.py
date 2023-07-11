from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="1. ¿Cuál es tu nombre?", widget=forms.TextInput(attrs={'placeholder': 'Juan Perez'}), max_length=100)
    email = forms.EmailField(label="2. ¿A que correo puedo contactarte?", widget=forms.TextInput(attrs={'placeholder': 'juan.perez@gmail.com'}),max_length=100)
    subject = forms.CharField(label="3. ¿En qué puedo ayudarte?", widget=forms.TextInput(attrs={'placeholder': 'Desarrollo Web, Aplicación Web'}), max_length=100)
    message = forms.CharField(label="4. ¿Podrías describirlo brevemente?", widget=forms.Textarea(attrs={'placeholder': 'Tengo un proyecto genial...'}))