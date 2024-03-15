from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Lucas', '10')
restaurante_praca.receber_avaliacao('Emy', '5')
restaurante_praca.receber_avaliacao('Guilherme', '8')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()