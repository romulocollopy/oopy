# coding: utf-8

"""
Código inicial usado na Lista de Exercícios 1 do curso
"Objetos Pythonicos" de Luciano Ramalho, Python.pro.br.
"""

class Contador(object):

    def __init__(self):
        self.ocorrencias = {}

    def incrementar(self, item):
        qtd = self.ocorrencias.get(item, 0) + 1
        self.ocorrencias[item] = qtd

    def contagem(self, item):
        return self.ocorrencias[item]

class ContadorAmigavel(Contador):

    def contagem(self, item):
        return self.ocorrencias.get(item, 0)

class ContadorTotalizador(Contador):

    def incrementar(self, item):
        qtd = self.ocorrencias.get(item, 0)+1
        self.ocorrencias[item] = qtd
        self.total = reduce(lambda x, y: x+y, self.ocorrencias.values())

    def porcentagem(self, item):
        return self.ocorrencias.get(item, 0)*100.0/self.total

class ContadorTotalizadorAmigavel(ContadorTotalizador, ContadorAmigavel):
    pass
