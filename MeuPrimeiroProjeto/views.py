from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def articles(request, year):
    return HttpResponse('O valor envaido foi: ' + str(year))

def lerDoBanco(nome):
    lista = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'joaquim', 'idade': 27},
    ]
    for pessoa in lista:
        if pessoa ['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade':0}

def fname(request, nome):
    resultado= lerDoBanco(nome)
    return HttpResponse('Nome: ' +  resultado['nome'] + ' Idade: ' + str(resultado['idade']))


def fname2(request, nome):
    resultado= lerDoBanco(nome)
    return render(request, 'pessoa.html', {'v_idade': resultado['idade']})    



