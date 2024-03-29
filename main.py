import time
#----------------------------------------------------------ZAPATOS--------------------------------------------------------------------------
class Zapatos:
    producto = ''
    precio = 0
    talla = ''

class Adidas(Zapatos):
    producto = 'Adidas'
    precio = 299
    talla = '9'

class NewBalance(Zapatos):
    producto = 'New Balance'
    precio = 249
    talla = '10'

class Nike(Zapatos):
    producto = 'Nike'
    precio = 199
    talla = '8'

#-----------------------------------------------------------CELULARES--------------------------------------------------------------------------
class Celulares:
    producto = ''
    precio = 0
    almacenamiento = ''
    procesador = ''
    sistema_operativo = ''
    memoria_ram = ''

class iPhone11(Celulares):
    producto = 'iPhone 11'
    precio = 2549
    almacenamiento = '128GB'
    procesador = 'A13 Bionic Chip'
    sistema_operativo = 'IOS'
    memoria_ram = '4GB'


class iPhone13(Celulares):
    producto = 'iPhone 13'
    precio = 3089
    almacenamiento = '128GB'
    procesador = 'A15 Bionic Chip'
    sistema_operativo = 'IOS'
    memoria_ram = '4GB'

class GalaxyS23(Celulares):
    producto = 'Samsung Galaxy S23 Ultra'
    precio = 5499
    almacenamiento = '256GB'
    procesador = 'Samsung Qualcomm SM8550'
    sistema_operativo = 'Android'
    memoria_ram = '12GB'

#------------------------------------------------------------INVENTARIO--------------------------------------------------------------------------
class Inventario:
    def __init__(self):
        pass

    def mostrar_info(self):
        pass
    
    """
    def mostrar_productos(self):
        for i,x in enumerate(self.pokemons):
            print(f'{i+1}) {pk.Pokemon(x()).ver_nombre()}')
    """

class Zapato_Inventario(Inventario):
    def __init__(self, zapato:Zapatos):
        self.zapato = zapato

    def mostrar_info(self):
        print(f'Producto: {self.zapato.producto}\n'
              f'Precio:   ${self.zapato.precio}\n'
              f'Talla:    {self.zapato.talla}')
        
    def precio(self):
        return self.zapato.precio

class Celular_Inventario(Inventario):
    def __init__(self, celular:Celulares):
        self.celular = celular

    def mostrar_info(self):
        print(f'Producto:          {self.celular.producto}\n'
              f'Precio:            ${self.celular.precio}\n'
              f'Almacenamiento:    {self.celular.almacenamiento}\n'
              f'Procesador:        {self.celular.procesador}\n'
              f'Sistema Operativo: {self.celular.sistema_operativo}\n'
              f'Memoria RAM:       {self.celular.memoria_ram}')
        
    def precio(self):
        return self.celular.precio
    
#------------------------------------------------------------LISTAS--------------------------------------------------------------------------
class ListaZapatos():
    def __init__(self):
        self.zapatos = [Adidas, NewBalance, Nike]

    def ver_lista_zapatos(self):
        for i, x in enumerate(self.zapatos):
            print(f'{i+1} {Zapato_Inventario(x()).mostrar_info()}\n')

#------------------------------------------------------------CARRITO--------------------------------------------------------------------------
class Carrito_cliente:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto:Inventario, cantidad):
        for i in range(cantidad):
            self.productos.append(producto)

    def mostrar_carrito(self):
        if len(self.productos) <= 0:
            print('\nCarrito de compras vacio\n'
                  'Te invitamos a revisar las diferentes categorias que tiene nuestra tienda\n'
                  'Volviendo al inicio...\n')
            time.sleep(2)
            main()
        else:
            precio_total = 0
            for i in self.productos:
                i.mostrar_info()
                precio_total += i.precio()
                print('\n')
            print(f'El precio total del carrito de compras es de ${precio_total}')

def main():
    cliente = Carrito_cliente()
    try:
        eleccion_cliente = int(input('Estas son las categorias disponibles:\n'
                                     '1. Zapatos\n'
                                     '2. Camisetas\n'
                                     '3. Celulares\n'
                                     '4. Televisores\n'
                                     '5. Ver carrito de compras\n'
                                     '6. Salir de la tienda\n'
                                     '¿Cual categoria deseas revisar?\n'))
    except ValueError:
        print('\nERROR\n'
              'Volviendo al inicio...\n')
        time.sleep(1)
        main()
    else:
        if eleccion_cliente == 1:
            ListaZapatos().ver_lista_zapatos()
        elif eleccion_cliente == 2:
            pass
        elif eleccion_cliente == 3:
            pass
        elif eleccion_cliente == 4:
            pass
        elif eleccion_cliente == 5:
            cliente.mostrar_carrito()
        elif eleccion_cliente == 6:
            time.sleep(1)
            exit('\nGracias por visitar nuestra tienda.\n')

if __name__ == "__main__":
    main()