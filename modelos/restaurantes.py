class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
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
     print(f'Nome do restaurante | Categoria | Status')
     for restaurante in cls.restaurantes:
       print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante._ativo}')


restaurante1 = Restaurante('Restaurante da Vovó', 'Comida Caseira')
restaurante2 = Restaurante('Chique', 'Gourmet')

Restaurante.listar_restaurantes()