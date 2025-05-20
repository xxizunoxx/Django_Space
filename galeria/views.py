from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar esta página.')
        return redirect('login')
    
    fotografias = Fotografia.objects.filter(publicado=True).order_by('data')
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar esta página.')
        return redirect('login')
    
    fotografias = Fotografia.objects.filter(publicado=True).order_by('data')
    if "buscar" in request.GET:
        termo = request.GET['buscar']
        if termo:
            fotografias = fotografias.filter(nome__icontains=termo)
            
    return render(request, 'galeria/buscar.html', {'cards': fotografias})