from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(label='Nome de Login', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: João Silva'}))
    password = forms.CharField(label='Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: 12345678'}))

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label='Nome Completo', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: João Silva'}))
    email = forms.EmailField(label='E-mail', required=True, max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex.:exemplo@exemplo.com.br'}))
    password1 = forms.CharField(label='Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: 12345678'}))
    password2 = forms.CharField(label='Confirmação de Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Digite novamente a senha'}))