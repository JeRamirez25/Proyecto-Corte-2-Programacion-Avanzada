import time
#
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
#
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
#
class Camisetas():
    producto = ''
    precio = 0
    talla = ''

class Koaj(Camisetas):
    producto = 'Koaj'
    precio = 79
    talla = 'S'

class AmericanEagle(Camisetas):
    producto = 'American Eagle'
    precio = 99
    talla = 'M'

class PoloClub(Camisetas):
    producto = 'Polo Club'
    precio = 149
    talla = 'XS'
#
class Audifinos():
    producto = ''
    precio = 0
    garantia = ''

class Sony(Audifinos):
    producto = 'Sony'
    precio = 399
    garantia = 'No posee garantia'

class JBL(Audifinos):
    producto = 'JBL'
    precio = 599
    garantia = '6 meses'

class AirPods(Audifinos):
    producto = 'AirPods'
    precio = 999
    garantia = '1 año'
#
class Inventario:
    def __init__(self):
        pass

    def mostrar_info(self):
        pass

    def precio(self):
        pass
    
class Zapato_Inventario(Inventario):
    def __init__(self, zapato: Zapatos):
        self.zapato = zapato

    def mostrar_info(self):
        print(f'Producto: {self.zapato.producto}\n'
              f'Precio:   ${self.zapato.precio}\n'
              f'Talla:    {self.zapato.talla}')
    
    def precio(self):
        return self.zapato.precio
 
class Celular_Inventario(Inventario):
    def __init__(self, celular: Celulares):
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
        
class Camiseta_Inventario(Inventario):
    def __init__(self, camiseta: Camisetas):
        self.camiseta = camiseta

    def mostrar_info(self):
        print(f'Producto: {self.camiseta.producto}\n'
              f'Precio:   ${self.camiseta.precio}\n'
              f'Talla:    {self.camiseta.talla}')
        
    def precio(self):
        return self.camiseta.precio
    
class Audifonos_Inventario(Inventario):
    def __init__(self, audifonos: Audifinos):
        self.audifonos = audifonos
    
    def mostrar_info(self):
        print(f'Producto: {self.audifonos.producto}\n'
              f'Precio:   ${self.audifonos.precio}\n'
              f'Garantia: {self.audifonos.garantia}')
        
    def precio(self):
        return self.audifonos.precio     
#
class ListaZapatos():
    def __init__(self):
        self.zapatos = [Adidas(), NewBalance(), Nike()]

    def ver_lista_zapatos(self):
        for i, x in enumerate(self.zapatos, start = 0):
            print(f'\n{i+1}.')
            Zapato_Inventario(x).mostrar_info()
            print('\n')

class ListaCelulares():
    def __init__(self):
        self.celulares = [iPhone11(), iPhone13(), GalaxyS23()]

    def ver_lista_celulares(self):
        for i, x in enumerate(self.celulares, start = 0):
            print(f'\n{i+1}.')
            Celular_Inventario(x).mostrar_info()
            print('\n')

class ListaCamisetas():
    def __init__(self):
        self.camisetas = [Koaj(), AmericanEagle(), PoloClub()]

    def ver_lista_camisetas(self):
        for i, x in enumerate(self.camisetas, start = 0):
            print(f'\n{i+1}.')
            Camiseta_Inventario(x).mostrar_info()
            print('\n')

class ListaAudifonos():
    def __init__(self):
        self.audifonos = [Sony(), JBL(), AirPods()]

    def ver_lista_audifonos(self):
        for i, x in enumerate(self.audifonos, start = 0):
            print(f'\n{i+1}.')
            Audifonos_Inventario(x).mostrar_info()
            print('\n')
#
class Carrito_cliente:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Inventario, cantidad):
        for i in range(cantidad):
            self.productos.append(producto)

    def mostrar_carrito(self):
        if len(self.productos) <= 0:
            print('\nCarrito de compras vacio\n'
                  'Te invitamos a revisar las diferentes categorias que tiene nuestra tienda\n'
                  'Volviendo al inicio...\n')
            time.sleep(2)
        else:
            precio_total = 0
            for i in self.productos:
                i.mostrar_info()
                precio_total += i.precio()
                print('\n')
            print(f'El precio total del carrito de compras es de ${precio_total}')

def main():
    cliente = Carrito_cliente()
    while True:
        try:
            eleccion_cliente = int(input('Estas son las categorias disponibles:\n'
                                        '1. Zapatos\n'
                                        '2. Camisetas\n'
                                        '3. Celulares\n'
                                        '4. Audifonos\n'
                                        '5. Ver carrito de compras\n'
                                        '6. Salir de la tienda\n'
                                        '¿Cual categoria deseas revisar?\n'))
            if eleccion_cliente == 1:
                ListaZapatos().ver_lista_zapatos()
                try:
                    eleccion_zapatos = int(input('¿Deseas agregar algun producto de esta categoria al carrito de compras?\n'
                                    '1. Si\n'
                                    '2. No\n'
                                    '3. Salir de la tienda\n'))
                    if eleccion_zapatos == 1:
                        try:
                            eleccion_zapatos_producto = int(input('Elija un tipo de zapatos\n'))-1
                            try:
                                eleccion_zapatos_cantidad = int(input('¿Cuantos pares necesita?\n'))
                                cliente.agregar_producto(Zapato_Inventario(ListaZapatos().zapatos[eleccion_zapatos_producto]), eleccion_zapatos_cantidad)
                            except ValueError:
                                pass
                        except ValueError:
                            pass
                    elif eleccion_zapatos == 2:
                        print('Volviendo al inicio...\n')
                        time.sleep(2)
                    elif eleccion_zapatos == 3:
                        time.sleep(1)
                        exit('\nGracias por visitar nuestra tienda.\n')
                    else:
                        print('\nLo siento, no te entendi\n')
                        time.sleep(1)
                except ValueError:
                    print('\nERROR\n'
                          'Volviendo al inicio...\n')
                    time.sleep(1)            
            elif eleccion_cliente == 2:
                ListaCamisetas().ver_lista_camisetas()
                try:
                    eleccion_camisetas = int(input('¿Deseas agregar algun producto de esta categoria al carrito de compras?\n'
                                                   '1. Si\n'
                                                   '2. No\n'
                                                   '3. Salir de la tienda\n'))
                    if eleccion_camisetas == 1:
                        try:
                            eleccion_camisetas_producto = int(input('Elija un tipo de camiseta:\n'))-1
                            try:
                                eleccion_camisetas_cantidad = int(input('¿Cuantas camisetas necesitas?\n'))
                                cliente.agregar_producto(Camiseta_Inventario(ListaCamisetas().camisetas[eleccion_camisetas_producto]), eleccion_camisetas_cantidad)
                            except ValueError:
                                pass
                        except ValueError:
                            pass
                    elif eleccion_camisetas == 2:
                        print('Volviendo al inicio...\n')
                        time.sleep(2)
                    elif eleccion_camisetas == 3:
                        time.sleep(1)
                        exit('\nGracias por visitar nuestra tienda.\n')
                    else:
                        print('\nLo siento, no te entendi\n')
                        time.sleep(1)
                except ValueError:
                    print('\nERROR\n'
                          'Volviendo al inicio...\n')
                    time.sleep(1)
            elif eleccion_cliente == 3:
                ListaCelulares().ver_lista_celulares()
                try:
                    eleccion_celulares = int(input('¿Deseas agregar algun producto de esta categoria al carrito de compras?\n'
                                                   '1. Si\n'
                                                   '2. No'
                                                   '3. Salir de la tienda\n'))
                    if eleccion_celulares == 1:
                        try:
                            eleccion_celulares_producto = int(input('Elija el tipo del celular que desea:\n'))-1
                            try:
                                eleccion_celulares_cantidad = int(input('¿Cuantos celulares necesitas?\n'))
                                cliente.agregar_producto(Celular_Inventario(ListaCelulares().celulares[eleccion_celulares_producto]), eleccion_celulares_cantidad)
                            except ValueError:
                                pass
                        except ValueError:
                            pass
                    elif eleccion_celulares == 2:
                        print('Volviendo al inicio...\n')
                        time.sleep(2)
                    elif eleccion_celulares == 3:
                        time.sleep(1)
                        exit('\nGracias por visitar nuestra tienda.\n')
                    else:
                        print('\nLo siento, no te entendi\n')
                        time.sleep(1)
                except ValueError:
                    print('\nERROR\n'
                          'Volviendo al inicio...\n')
                    time.sleep(1)
            elif eleccion_cliente == 4:
                ListaAudifonos().ver_lista_audifonos()
                try:
                    eleccion_audifonos = int(input('¿Deseas agregar algun producto de esta categoria al carrito de compras?\n'
                                                   '1. Si\n'
                                                   '2. No'
                                                   '3. Salir de la tienda\n'))
                    if eleccion_audifonos == 1:
                        try:
                            eleccion_audifonos_producto = int(input('Elija el tipo de audifonos que desea:\n'))-1
                            try:
                                eleccion_audifonos_cantidad = int(input('¿Cuantos celulares necesitas?\n'))
                                cliente.agregar_producto(Audifonos_Inventario(ListaAudifonos().audifonos[eleccion_audifonos_producto]), eleccion_audifonos_cantidad)
                            except ValueError:
                                pass
                        except ValueError:
                            pass
                    elif eleccion_audifonos == 2:
                        print('Volviendo al inicio...\n')
                        time.sleep(2)
                    elif eleccion_audifonos == 3:
                        time.sleep(1)
                        exit('\nGracias por visitar nuestra tienda.\n')
                    else:
                        print('\nLo siento, no te entendi\n')
                        time.sleep(1)
                except ValueError:
                    print('\nERROR\n'
                          'Volviendo al inicio...\n')
                    time.sleep(1)
            elif eleccion_cliente == 5:
                cliente.mostrar_carrito()
            elif eleccion_cliente == 6:
                time.sleep(1)
                exit('\nGracias por visitar nuestra tienda.\n')
            else:
                print('\nLo siento, no te entendi\n')
                time.sleep(1)
        except ValueError:
            print('\nERROR\n'
                  'Volviendo al inicio...\n')
            time.sleep(1)
      
if __name__ == "__main__":
    main()