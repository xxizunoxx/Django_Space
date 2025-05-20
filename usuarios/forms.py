from django import forms
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    nome_login = forms.CharField(label='Login', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: João Silva'}))
    password = forms.CharField(label='Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: 12345678'}))

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label='Usúario', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: João_Silva'}))
    email = forms.EmailField(label='E-mail', required=True, max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex.:exemplo@exemplo.com.br'}))
    password1 = forms.CharField(label='Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: 12345678'}))
    password2 = forms.CharField(label='Confirmação de Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Digite novamente a senha'}))

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('O nome não pode conter espaços em branco.')
            else:
                return nome
        
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('As senhas não conferem.')
            else:
                return password2