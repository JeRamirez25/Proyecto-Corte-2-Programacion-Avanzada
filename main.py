"""
JUAN ESTEBAN RAMIREZ GALAN CC.1014977669
PROGRAMACION AVANZADA 2024-1S
CORTE 2
PROYECTO TIENDA
"""

import time

"""
SE CREA LA CLASE ZAPATOS CON SUS DIFERENTES PRODUCTOS
"""

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

class Merrel(Zapatos):
    producto = 'Merrel'
    precio = 499
    talla = '8.5'

class Croydon(Zapatos):
    producto = 'Croydon'
    precio = 149
    talla = '7'

"""
SE CREA LA CLASE CELULARES CON SUS DIFERENTES PRODUCTOS
"""

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

class iPhone14(Celulares):
    producto = 'iPhone 14'
    precio = 3999
    almacenamiento = '128GB'
    procesador = 'A15 Bionic Chip'
    sistema_operativo = 'IOS'
    memoria_ram = '6GB'

class iPhone15(Celulares):
    producto = 'iPhone 15'
    precio = 4599
    almacenamiento = '128GB'
    procesador = 'A16 Bionic Chip'
    sistema_operativo = 'IOS'
    memoria_ram = '6GB'

"""
SE CREA LA CLASE CAMISETAS CON SUS DIFERENTES PRODUCTOS
"""

class Camisetas:
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

class RoottCo(Camisetas):
    producto = 'Roott+Co'
    precio = 89
    talla = 'L'

class ArturoCalle(Camisetas):
    producto = 'Arturo Calle'
    precio = 129
    talla = 'XL'

"""
SE CREA LA CLASE AUDIFONOS CON SUS DIFERENTES PRODUCTOS
"""

class Audifinos:
    producto = ''
    precio = 0
    modelo = ''
    garantia = ''

class Sony(Audifinos):
    producto = 'Sony'
    precio = 299
    modelo = 'WF-C500'
    garantia = '30 dias'

class JBL(Audifinos):
    producto = 'JBL'
    precio = 469
    modelo = 'JBLTFLEXBLU'
    garantia = '6 meses'

class Apple(Audifinos):
    producto = 'AirPods Pro Generacion 2'
    precio = 1399
    modelo = 'MTJV3AM/A'
    garantia = '1 año'

class AKG(Audifinos):
    producto = 'AKG'
    precio = 349
    modelo = 'N20BLK'
    garantia = '6 meses'

class Beats(Audifinos):
    producto = 'Beats'
    precio = 899
    modelo = 'FIT PRO'
    garantia = '1 año'

"""
SE CREA LA CLASE NEVERAS CON SUS DIFERENTES PRODUCTOS
"""

class Neveras:
    producto = ''
    precio = 0
    capacidad_total = ''
    alto = ''
    ancho = ''
    profundidad = ''
    dispensador_agua = ''
    dispensador_hielo = ''

class NeveconLG(Neveras):
    producto = 'Nevecon LG'
    precio = 8289
    capacidad_total = '637 Litros'
    alto = '178.5 cm'
    ancho = '91.2 cm'
    profundidad = '73.5 cm'
    dispensador_agua = 'Automatico'
    dispensador_hielo = 'Automatico'

class WhirlPool(Neveras):
    producto = 'WhirlPool'
    precio = 1699
    capacidad_total = '234 Litros'
    alto = '151 cm'
    ancho = '67.1 cm'
    profundidad = '75.5 cm'
    dispensador_agua = 'No aplica'
    dispensador_hielo = 'Manual'

class NeveconSamsung(Neveras):
    producto = 'Nevecon Samsung'
    precio = 4999
    capacidad_total = '788 Litros'
    alto = '177.7 cm'
    ancho = '90.8 cm'
    profundidad = '83.6 cm'
    dispensador_agua = 'Manual'
    dispensador_hielo = 'Automatico'

class Samsung(Neveras):
    producto = 'Samsung'
    precio = 2379
    capacidad_total = '345 Litros'
    alto = '171.5 cm'
    ancho = '60 cm'
    profundidad = '70.9 cm'
    dispensador_agua = 'Manual'
    dispensador_hielo = 'No aplica'

class LG(Neveras):
    producto = 'LG'
    precio = 2859
    capacidad_total = '374 Litros'
    alto = '172 cm'
    ancho = '70 cm'
    profundidad = '68 cm'
    dispensador_agua = 'Manual'
    dispensador_hielo = 'Manual'

"""
SE CREA LA CLASE NEVERAS CON SUS DIFERENTES PRODUCTOS
"""

class Televisores:
    producto = ''
    precio = 0
    tamaño_pantalla = ''
    caracteristicas_pantalla = ''
    modelo = ''
    tasa_refresco = ''
    garantia = ''

class TvLG(Televisores):
    producto = 'LG'
    precio = 2049
    tamaño_pantalla = '60 Pulgadas'
    caracteristicas_pantalla = 'LED'
    modelo = '60UQ8050PSB.AWC'
    tasa_refresco = '60 Hz'
    garantia = '1 año'

class TvSamgung(Televisores):
    producto = 'Samsung'
    precio = 1899
    tamaño_pantalla = '58 Pulgadas'
    caracteristicas_pantalla = 'Crystal UHD'
    modelo = 'UN58CU7000KXZL'
    tasa_refresco = '60 Hz'
    garantia = '1 año'

class Caixun(Televisores):
    producto = 'Caixun'
    precio = 1699
    tamaño_pantalla = '55 Pulgadas'
    caracteristicas_pantalla = 'LED'
    modelo = 'C55VAUG'
    tasa_refresco = '60 Hz'
    garantia = '2 años'

class Challenger(Televisores):
    producto = 'Challenger'
    precio = 1699
    tamaño_pantalla = '58 Pulgadas'
    caracteristicas_pantalla = 'LED'
    modelo = '58LO70'
    tasa_refresco = '60 Hz'
    garantia = '1 año'

class Hyundai(Televisores):
    producto = 'Hyundai'
    precio = 969
    tamaño_pantalla = '43 Pulgadas'
    caracteristicas_pantalla = 'LED'
    modelo = 'HYLED4322GiM'
    tasa_refresco = '60 Hz'
    garantia = '1 año'

"""
SE CREA LA CLASE INVENTARIO CON SUS SUBCLASES PARA PODER ANALIZAR Y ESTRUCTURAR
LOS PRODUCTOS DE CADA UNA DE LAS CATEGORIAS QUE POSEE LA TIENDA VIRTUAL
"""

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
              f'Modelo:   {self.audifonos.modelo}\n'
              f'Garantia: {self.audifonos.garantia}')
        
    def precio(self):
        return self.audifonos.precio
    
class Neveras_Inventario(Inventario):
    def __init__(self, nevera: Neveras):
        self.nevera = nevera

    def mostrar_info(self):
        print(f'Producto:             {self.nevera.producto}\n'
              f'Precio:               ${self.nevera.precio}\n'
              f'Capacidad total:      {self.nevera.capacidad_total}\n'
              f'Alto:                 {self.nevera.alto}\n'
              f'Ancho:                {self.nevera.ancho}\n'
              f'Profundidad:          {self.nevera.profundidad}\n'
              f'Dispensador de agua:  {self.nevera.dispensador_agua}\n'
              f'Dispensador de hielo: {self.nevera.dispensador_hielo}\n')
        
    def precio(self):
        return self.nevera.precio
    
class Televisores_Inventario(Inventario):
    def __init__(self, televisor: Televisores):
        self.televisor = televisor
    
    def mostrar_info(self):
        print(f'Producto:                       {self.televisor.producto}\n'
              f'Precio:                         ${self.televisor.precio}\n'
              f'Tamaño de la pantalla:          {self.televisor.tamaño_pantalla}\n'
              f'Caracteristicas de la pantalla: {self.televisor.caracteristicas_pantalla}\n'
              f'Modelo:                         {self.televisor.modelo}\n'
              f'Tasa de refresco:               {self.televisor.tasa_refresco}\n'
              f'Garantia:                       {self.televisor.garantia}\n')
    
    def precio(self):
        return self.televisor.precio

"""
SE CREAN CLASES LLAMADAS LISTAS PARA RECORRER LOS INVENTARIOS DE CADA
CATEGORIA Y DE ESTA MANERA MOSTRARLOS CUANDO EL USUARIO LO SOLICITE
"""

class ListaZapatos:
    def __init__(self):
        self.zapatos = [Adidas(), NewBalance(), Nike(), Merrel(), Croydon()]

    def ver_lista_zapatos(self):
        for i, x in enumerate(self.zapatos, start = 0):
            print(f'\n{i+1}.')
            Zapato_Inventario(x).mostrar_info()
            print('\n')

class ListaCelulares:
    def __init__(self):
        self.celulares = [iPhone11(), iPhone13(), GalaxyS23(), iPhone14(), iPhone15()]

    def ver_lista_celulares(self):
        for i, x in enumerate(self.celulares, start = 0):
            print(f'\n{i+1}.')
            Celular_Inventario(x).mostrar_info()
            print('\n')

class ListaCamisetas:
    def __init__(self):
        self.camisetas = [Koaj(), AmericanEagle(), PoloClub(), ArturoCalle(), RoottCo()]

    def ver_lista_camisetas(self):
        for i, x in enumerate(self.camisetas, start = 0):
            print(f'\n{i+1}.')
            Camiseta_Inventario(x).mostrar_info()
            print('\n')

class ListaAudifonos:
    def __init__(self):
        self.audifonos = [Sony(), JBL(), Apple(), AKG(), Beats()]

    def ver_lista_audifonos(self):
        for i, x in enumerate(self.audifonos, start = 0):
            print(f'\n{i+1}.')
            Audifonos_Inventario(x).mostrar_info()
            print('\n')

class ListaNeveras:
    def __init__(self):
        self.neveras = [NeveconLG(), NeveconSamsung(), Samsung(), LG(), WhirlPool()]

    def ver_lista_neveras(self):
        for i, x in enumerate(self.neveras, start = 0):
            print(f'\n{i+1}.')
            Neveras_Inventario(x).mostrar_info()
            print('\n')

class ListaTelevisores:
    def __init__(self):
        self.televisores = [TvLG(), TvSamgung(), Caixun(), Challenger(), Hyundai()]

    def ver_lista_televisores(self):
        for i, x in enumerate(self.televisores, start = 0):
            print(f'\n{i+1}.')
            Televisores_Inventario(x).mostrar_info()
            print('\n')

"""
SE CREA LA CLASE CARRITO DE COMPRAS EN LA CUAL MEDIANTE FUNCIONES
PODEMOS HACER QUE SE AGREGUEN PRODUCTOS AL CARRITO DE COMPRAS Y
MOSTRAR LOS PRODUCTOS QUE YA HAN SIDO AGREGADOS
"""

class Carrito_cliente:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Inventario, cantidad):
        for i in range(cantidad):
            self.productos.append(producto)
        print('\nProducto/s agregado/s al carrito de compras.\n')

    def mostrar_carrito(self):
        if len(self.productos) <= 0:
            print('\nCarrito de compras vacio\n'
                  'Te invitamos a revisar las diferentes categorias que tiene nuestra tienda\n'
                  'Volviendo al inicio...\n')
            time.sleep(2)
        else:
            precio_total = 0
            print('\n')
            for i in self.productos:
                i.mostrar_info()
                precio_total += i.precio()
                print('\n')
            print(f'El precio total del carrito de compras es de ${precio_total}\n')

"""
SE CREAN DIFERENTES FUNCIONES QUE COMPLEMENTAN A LA FUNCION
MAIN PARA EL FUNCIONAMIENTO DEL CODIGO
"""

def eleccion_zapatos():
    try:
        eleccion_zapatos = int(input('\n¿Deseas agregar algun producto de esta categoria al carrito de compras?\n'
                                        '1. Si\n'
                                        '2. No\n'
                                        '3. Salir de la tienda\n'))
        if eleccion_zapatos == 1:
            try:
                eleccion_zapatos_producto = int(input('\nElija un tipo de zapatos:\n'))-1
                try:
                    eleccion_zapatos_cantidad = int(input('\n¿Cuantos pares de zapatos necesita?\n'))
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

def eleccion_camisetas():
    try:
        eleccion_camisetas = int(input('\n¿Deseas agregar algun producto de esta categoria al carrito de compras?\n'
                                        '1. Si\n'
                                        '2. No\n'
                                        '3. Salir de la tienda\n'))
        if eleccion_camisetas == 1:
            try:
                eleccion_camisetas_producto = int(input('\nElija un tipo de camiseta:\n'))-1
                try:
                    eleccion_camisetas_cantidad = int(input('\n¿Cuantas camisetas necesitas?\n'))
                    cliente.agregar_producto(Camiseta_Inventario(ListaCamisetas().camisetas[eleccion_camisetas_producto]), eleccion_camisetas_cantidad)
                except ValueError:
                    pass
            except ValueError:
                pass
        elif eleccion_camisetas == 2:
            print('\nVolviendo al inicio...\n')
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

def eleccion_celulares():
    try:
        eleccion_celulares = int(input('\n¿Deseas agregar algun producto de esta categoria al carrito de compras?\n'
                                        '1. Si\n'
                                        '2. No\n'
                                        '3. Salir de la tienda\n'))
        if eleccion_celulares == 1:
            try:
                eleccion_celulares_producto = int(input('\nElija el tipo del celular que desea:\n'))-1
                try:
                    eleccion_celulares_cantidad = int(input('\n¿Cuantos celulares necesitas?\n'))
                    cliente.agregar_producto(Celular_Inventario(ListaCelulares().celulares[eleccion_celulares_producto]), eleccion_celulares_cantidad)
                except ValueError:
                    pass
            except ValueError:
                pass
        elif eleccion_celulares == 2:
            print('\nVolviendo al inicio...\n')
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

def eleccion_audifonos():
    try:
        eleccion_audifonos = int(input('\n¿Deseas agregar algun producto de esta categoria al carrito de compras?\n'
                                        '1. Si\n'
                                        '2. No\n'
                                        '3. Salir de la tienda\n'))
        if eleccion_audifonos == 1:
            try:
                eleccion_audifonos_producto = int(input('\nElija el tipo de audifonos que desea:\n'))-1
                try:
                    eleccion_audifonos_cantidad = int(input('\n¿Cuantos audifonos necesitas?\n'))
                    cliente.agregar_producto(Audifonos_Inventario(ListaAudifonos().audifonos[eleccion_audifonos_producto]), eleccion_audifonos_cantidad)
                except ValueError:
                    pass
            except ValueError:
                pass
        elif eleccion_audifonos == 2:
            print('\nVolviendo al inicio...\n')
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

def eleccion_televisores():
    try:
        eleccion_televisores = int(input('\n¿Deseas agregar algun producto de esta categoria al carrito de compras?\n'
                                            '1. Si\n'
                                            '2. No\n'
                                            '3. Salir de la tienda\n'))
        if eleccion_televisores == 1:
            try:
                eleccion_televisores_producto = int(input('\nElija el tipo de televisor que desea:\n'))-1
                try:
                    eleccion_televisores_cantidad = int(input('\n¿Cuantos televisores necesitas?\n'))
                    cliente.agregar_producto(Televisores_Inventario(ListaTelevisores().televisores[eleccion_televisores_producto]), eleccion_televisores_cantidad)
                except ValueError:
                    pass
            except ValueError:
                pass
        elif eleccion_televisores == 2:
            print('\nVolviendo al inicio...\n')
            time.sleep(2)
        elif eleccion_televisores == 3:
            time.sleep(1)
            exit('\nGracias por visitar nuestra tienda.\n')
        else:
            print('\nLo siento, no te entendi\n')
            time.sleep(1)
    except ValueError:
        print('\nERROR\n'
                'Volviendo al inicio...\n')
        time.sleep(1)

def eleccion_neveras():
    try:
        eleccion_nevera = int(input('\n¿Deseas agregar algun producto de esta categoria al carrito de compras?\n'
                                    '1. Si\n'
                                    '2. No\n'
                                    '3. Salir de la tienda\n'))
        if eleccion_nevera == 1:
            try:
                eleccion_nevera_producto = int(input('\nElija el tipo de nevera que desea:\n'))-1
                try:
                    eleccion_nevera_cantidad = int(input('\n¿Cuantas neveras necesitas?\n'))
                    cliente.agregar_producto(Neveras_Inventario(ListaNeveras().neveras[eleccion_nevera_producto]), eleccion_nevera_cantidad)
                except ValueError:
                    pass
            except ValueError:
                pass
        elif eleccion_audifonos == 2:
            print('\nVolviendo al inicio...\n')
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

"""
SE CREA UNA FUNCION MAIN PARA PODER INICIALIZAR LA EJECUCION DEL
CODIGO Y DE LA TIENDA VIRTUAL, EN LA CUAL SE IMPLEMENTA MANEJO DE
EXCEPCIONES PARA MINIMIZAR CUALQUIER ERROR COMETIDO POR EL USUARIO
DURANTE LA EJECUCION DEL PROGRAMA
"""

def main():
    while True:
        try:
            eleccion_cliente = int(input('\nEstas son las categorias disponibles:\n'
                                         '1. Zapatos\n'
                                         '2. Camisetas\n'
                                         '3. Celulares\n'
                                         '4. Audifonos\n'
                                         '5. Televisores\n'
                                         '6. Neveras\n'
                                         '7. Ver carrito de compras\n'
                                         '8. Salir de la tienda\n'
                                         '¿Cual categoria deseas revisar?\n'))
            if eleccion_cliente == 1:
                ListaZapatos().ver_lista_zapatos()
                eleccion_zapatos()
            elif eleccion_cliente == 2:
                ListaCamisetas().ver_lista_camisetas()
                eleccion_camisetas()
            elif eleccion_cliente == 3:
                ListaCelulares().ver_lista_celulares()
                eleccion_celulares()
            elif eleccion_cliente == 4:
                ListaAudifonos().ver_lista_audifonos()
                eleccion_audifonos()
            elif eleccion_cliente == 5:
                ListaTelevisores().ver_lista_televisores()
                eleccion_televisores()
            elif eleccion_cliente == 6:
                ListaNeveras().ver_lista_neveras()
                eleccion_neveras()
            elif eleccion_cliente == 7:
                cliente.mostrar_carrito()
            elif eleccion_cliente == 8:
                time.sleep(1)
                exit('\nGracias por visitar nuestra tienda.\n')
            else:
                print('\nLo siento, no te entendi\n')
                time.sleep(1)
        except ValueError:
            print('\nERROR\n'
                  'Volviendo al inicio...\n')
            time.sleep(1)
    
"""
SE LLAMA LA FUNCION MAIN PARA EMPEZAR LA EJECUCION DEL PROGRAMA
"""

if __name__ == "__main__":
    cliente = Carrito_cliente()
    main()