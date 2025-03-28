from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante1 = Restaurante('Restaurante da Vovó', 'Comida Caseira')
bebida = Bebida('cafézinho', 5.00, 'pequeno')
prato = Prato('Pão de Queijo', 6.00, 'Pão de queijo caseiro')
bebida.aplicar_desconto()
prato.aplicar_desconto()
restaurante1.adicionar_no_cardapio(bebida)
restaurante1.adicionar_no_cardapio(prato)

def main():
    restaurante1.exibir_cardapio()

if __name__ == '__main__':
    main()