from django.shortcuts import render, redirect
from .models import Contato

def home(request):
    # Busca todos os contatos do banco para exibir na tela
    contatos = Contato.objects.all()
    return render(request, 'contatos/home.html', {'contatos': contatos})

def salvar(request):
    if request.method == 'POST':
        nome_front = request.POST.get('nome')
        email_front = request.POST.get('email')
        
        # A "cola" com o Banco: Criando o registro
        Contato.objects.create(nome=nome_front, email=email_front)
        
    return redirect('home')

def excluir(request, id):
    contato = Contato.objects.get(id=id) # Busca o contato específico
    contato.delete() # Deleta do banco de dados
    return redirect('home') # Volta para a página inicial