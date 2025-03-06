from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'

    def alternar_estado(self):
        self._ativo =  not self._ativo

    @classmethod
    def listar_restaurantes(cls):
     print(f'Nome do restaurante | Categoria | Avaliação | Status')
     for restaurante in cls.restaurantes:
       print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante.media_avaliacoes} | {restaurante._ativo}')

    def recebe_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0

        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas =  len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

