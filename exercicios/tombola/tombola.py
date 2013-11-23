from random import shuffle
from inplace import pairswap

class Tombola(object):
    '''Sorteia itens sem repetir'''

    def carregar(self, seq):
        self.itens = list(seq)

    def misturar(self, funcao_misturadora=None):
        if funcao_misturadora == None:
            shuffle(self.itens)
        else:
            funcao_misturadora(self.itens)
    def sortear(self):
        return self.itens.pop()

    def carregada(self):
        return bool(self.itens)

    def __iter__(self):
        for i in reversed(self.itens):
            yield i
