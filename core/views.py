from django.shortcuts import render

	# Create your views here.
	# Funções com as Rotas 
	# - Função index faz a requisição no arquivo index.html
	# - Função contato faz a requisição no arquivo contato.html
def index (request):
    return render(request, 'index.html')

def carro(request):
    return render(request, 'carro.html')

def contato (request):
    return render(request, 'contato.html')

