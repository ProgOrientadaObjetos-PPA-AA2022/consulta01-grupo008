class Ecuador:
    def sonido(self):
        print('Ecuador!!!')


class Colombia:
    def sonido(self):
        print('Colombia!!!')


class Perú:
    def sonido(self):
        print('Perú!!!')

def estadio(paises):
    for pais in paises:
        pais.sonido()

if __name__ == '__main__':
    ecuador = Ecuador()
    colombia = Colombia()
    colombia2 = Colombia()
    peru = Perú()
    ecuador2 = Ecuador()
    fanáticos = [ecuador, colombia, peru, colombia2, ecuador2]
    estadio(fanáticos)