class IProducto:
    def seleccionar(self):
        pass

class Zapatos(IProducto):
    def seleccionar(self):
        print("\n")
        zapatos_productos = ['Adidas', 'Nike', 'New Balance']
        zapatos_precios = [299, 249, 199]
        numero_producto = 1
        print('¡TODOS LOS PRECIOS DE LOS PRODUCTOS ESTAN MOSTRADOS EN MILES DE PESOS!')
        for i in range(len(zapatos_precios)):
            print(f"{numero_producto}. {zapatos_productos[i]} tiene un precio de {zapatos_precios[i]}")
            numero_producto += 1
        print("\n")
        try:
            eleccion_carrito = int(input("¿Deseas agergar algun producto al carrito de compras? \n"
                                + "1. Si \n"
                                + "2. Volver al inicio \n"
                                + "3. Salir de la tienda \n"))
        except ValueError:
            print("\nLo siento, no te entendí\n")
            main()
        else:
            if eleccion_carrito == 1:
                print("\n")
                try:
                    eleccion_producto = int(input("Indique el numero del producto que desea agregar: \n"))
                except ValueError:
                    print("\nLo siento, no te entendí\n")
                    main()
                else:
                    if eleccion_producto <= 0 or eleccion_producto > len(zapatos_precios):
                        print("\nError...")
                        print("Volviendo al inicio...\n")
                        main()
                    else:
                        try:
                            cantidad_productos = int(input("Escriba la cantidad deseada del producto agregar a su compra: \n"))
                        except ValueError:
                            print("\nLo siento, no te entendí\n")
                            main()
                        else:
                            if cantidad_productos > 0:
                                carrito = Carrito_compras()
                                for i in range(cantidad_productos):
                                    carrito.agregar_producto(zapatos_productos[eleccion_producto-1], zapatos_precios[eleccion_producto-1])
                                main()
                            else:
                                print("\nLo siento, no se pueden agregar 0 productos\n")
                                main()
            elif eleccion_carrito == 2:
                main()
            elif eleccion_carrito == 3:
                exit("Gracias por visitar nuestra tienda.")
            else:
                print("\nLo siento, no te entendí\n")
                main()
 
class Camisetas(IProducto):
    camisetas = {}
    def seleccionar(self):
        print("a")

class Pantalones(IProducto):
    pantalones = {}
    def seleccionar(self):
        print("a")
    
class Sacos(IProducto):
    sacos = {}
    def seleccionar(self):
        print("a")
    
class Carrito_compras:
    def __init__(self):
        self.productos = ['A','B']
        self.precios = [4,3]

    def agregar_producto(self, producto, valor):
        self.productos.append(producto)
        self.precios.append(valor)

    def ver_carrito(self):
        print("\n¡Los valores de los productos agregados en su carrito de compras estan dados en miles de pesos!\n")
        print("Los productos en su carrito son los siguientes:")
        for elemento in self.productos:
            print(elemento)
        print(f"\nEl precio total de los productos en el carrito es de {self.calcular_precio()}")

    def calcular_precio(self):
        total = sum(self.precios)
        return total
    
    def terminar_compra(self):
        pass

def main():
    try:
        eleccion_main = int(input("Estos son las categorias que tenemos disponibles: \n"
                                    + "1. Pantalones \n"
                                    + "2. Camisetas \n"
                                    + "3. Zapatos \n"
                                    + "4. Sacos \n"
                                    + "5. Carrito de compras \n"
                                    + "6. Salir de la tienda \n"
                                    + "¿Cual categoria deseas revisar? \n"))
    except ValueError:
        print("\n Lo siento, no te entendí \n")
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
            carrito = Carrito_compras()
            carrito.ver_carrito()
        elif eleccion_main == 6:
            exit("Gracias por visitar nuestra tienda.")
        else:
            print("\nLo siento, no te entendí\n")
            main()

if __name__ == "__main__":
    main()
