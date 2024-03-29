import time

class IProducto:
    def seleccionar(self):
        pass

class Zapatos(IProducto):
    def seleccionar(self):
        print("\n")
        zapatos_productos = ['Adidas', 'Nike', 'New Balance']
        zapatos_precios = [299, 249, 199]
        zapatos_descripcion = ['Talla 9', 'Talla 8', 'Talla 7']
        numero_producto = 1
        for i in range(len(zapatos_precios)):
            print(f"{numero_producto}. {zapatos_productos[i]} tiene un precio de ${zapatos_precios[i]}.000: {zapatos_descripcion[i]}")
            numero_producto += 1
        print("\n")
        try:
            eleccion_carrito = int(input("¿Deseas agregar algun producto al carrito de compras? \n"
                                + "1. Si \n"
                                + "2. Volver al inicio \n"
                                + "3. Salir de la tienda \n"))
        except ValueError:
            print("\nLo siento, no te entendí\n"
                  + "Volviendo al inicio...\n")
            time.sleep(2)
            main()
        else:
            if eleccion_carrito == 1:
                print("\n")
                try:
                    eleccion_producto = int(input("Indique el numero del producto que desea agregar: \n"))
                except ValueError:
                    print("\nLo siento, no te entendí\n"
                          + "Volviendo al inicio...\n")
                    time.sleep(2)
                    main()
                else:
                    if eleccion_producto <= 0 or eleccion_producto > len(zapatos_precios):
                        print("\nError...")
                        print("Volviendo al inicio...\n")
                        time.sleep(2)
                        main()
                    else:
                        try:
                            cantidad_productos = int(input("Escriba la cantidad deseada del producto agregar a su compra: \n"))
                        except ValueError:
                            print("\nLo siento, no te entendí\n"
                                  + "Volviendo al inicio...\n")
                            time.sleep(2)
                            main()
                        else:
                            if cantidad_productos > 0:
                                while i <= cantidad_productos:
                                    Carrito_compras().agregar_producto(zapatos_productos[eleccion_producto-1], zapatos_precios[eleccion_producto-1], zapatos_descripcion[eleccion_producto-1])
                                    i+=1
                                print("Producto/s agregado/s\n"
                                    + "Volviendo al inicio...\n")
                                time.sleep(2)
                                main()
                            else:
                                print("\nLo siento, no se pueden agregar 0 productos\n"
                                      + "Volviendo al inicio...\n")
                                time.sleep(2)
                                main()
            elif eleccion_carrito == 2:
                print("Volviendo al inicio...\n")
                time.sleep(2)
                main()
            elif eleccion_carrito == 3:
                exit("Gracias por visitar nuestra tienda.")
            else:
                print("\nLo siento, no te entendí\n"
                      + "Volviendo al inicio...\n")
                time.sleep(2)
                main()
 
class Camisetas(IProducto):
    def seleccionar(self):
        camisetas_productos = []
        camisetas_precios = []
        camisetas_descripcion = []
        pass

class Pantalones(IProducto):
    def seleccionar(self):
        pantalones_productos = []
        pantalones_precios = []
        pantalones_descripcion = []
        pass
    
class Sacos(IProducto):
    def seleccionar(self):
        sacos_productos = []
        sacos_precios = []
        sacos_descripcion = []
        pass

class Celulares(IProducto):
    def seleccionar(self):
        celulares_productos = []
        celulares_precios = []
        celulares_descripcion = []
        pass

class Televisores(IProducto):
    def seleccionar(self):
        televisores_productos = []
        televisores_precios = []
        televisores_descripcion = []
        pass

class Audifonos(IProducto):
    def seleccionar(self):
        audifonos_productos = []
        audifonos_precios = []
        audifonos_descripcion = []
        pass
    
class Carrito_compras:
    def __init__(self):
        self.productos = []
        self.precios = []
        self.descripcion = []

    def agregar_producto(self, producto, valor, descripcion):
        self.productos.append(producto)
        self.precios.append(valor)
        self.descripcion.append(descripcion)

    def ver_carrito(self):
        if len(self.descripcion) <= 0:
            print("\nSu carrito esta vacio.\n"
                  +"Volviendo al inicio...\n")
            time.sleep(2)
            main()
        else:
            print("\nLos productos en su carrito son los siguientes:")
            for i in range(len(self.descripcion)):
                print(f"{self.productos[i]} ${self.precios[i]}.000: {self.descripcion[i]}")
            print(f"\nEl precio total de los productos en el carrito es de ${self.calcular_precio()}.000")
    
    def calcular_precio(self):
        total = sum(self.precios)
        return total
    
    def terminar_compra(self):
        if len(self.precios) <= 0:
            pass

def main():
    try:
        eleccion_main = int(input("Estos son las categorias que tenemos disponibles: \n"
                                    + "1. Pantalones \n"
                                    + "2. Camisetas \n"
                                    + "3. Zapatos \n"
                                    + "4. Sacos \n"
                                    + "5. Celulares \n"
                                    + "6. Televisores \n"
                                    + "7. Audifonos \n"
                                    + "8. Carrito de compras \n"
                                    + "9. Finalizar compra \n"
                                    + "0. Salir de la tienda \n"
                                    + "¿Cual categoria deseas revisar? \n"))
    except ValueError:
        print("\n Lo siento, no te entendí \n"
              + "Volviendo al inicio...\n")
        time.sleep(2)
        main()
    else:
        if eleccion_main == 1:
            Pantalones().seleccionar()
        elif eleccion_main == 2:
            Camisetas().seleccionar()
        elif eleccion_main == 3:
            Zapatos().seleccionar()
        elif eleccion_main == 4:
            Sacos().seleccionar()
        elif eleccion_main == 5:
            Celulares().seleccionar()
        elif eleccion_main == 6:
            Televisores().seleccionar()
        elif eleccion_main == 7:
            Audifonos().seleccionar()
        elif eleccion_main == 8:
            Carrito_compras().ver_carrito()
        elif eleccion_main == 9:
            Carrito_compras().terminar_compra()
        elif eleccion_main == 0:
            exit("Gracias por visitar nuestra tienda.")
        else:
            print("\nLo siento, no te entendí\n"
                  + "Volviendo al inicio...\n")
            time.sleep(2)
            main()

if __name__ == "__main__":
    main()