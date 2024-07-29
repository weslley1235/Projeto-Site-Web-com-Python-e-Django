
from django.urls import path
#foi feito o importe do include acima
from core.views import index,carro,contato

urlpatterns = [
    path('', index, name='index'),
    path('carro', carro, name='carro'),
    path('contato', contato, name='contato'),
]
# acima o "path('', index)" indica que quando acessar a raiz do site será chamado a view index
# o "path('contato', contato)" indica que quando acessar a rota contato será chamado a view contato