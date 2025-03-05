from modelos.restaurante import Restaurante

restaurante1 = Restaurante('Restaurante da Vovó', 'Comida Caseira')
restaurante2 = Restaurante('Restaurante Chiquérimo', 'Gourmet')
restaurante1.recebe_avaliacao('Nika', 10)
restaurante1.recebe_avaliacao('Jake', 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()