import requests

class Carrito:
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto_data):
        id = str(producto_data['producto']['id'])
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "serie_del_producto": producto_data['producto']['serie_del_producto'],
                "nombre": producto_data['producto']['nombre'],
                "stock": producto_data['producto']['stock'],
                "precio": producto_data['producto']['precio'],
                "cantidad": 1,
                "imagen": producto_data['producto'].get('imagen'),
                "acumulado": producto_data['producto']['precio'],
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto_data['producto']['precio']
            self.carrito[id]["stock"] -= 1
        self.actualizar_total()  # Actualizar el total a pagar
        self.guardar_carrito()

    def get_productos(self):
        productos = []

        for producto_id, producto_info in self.carrito.items():
            # Obtener información adicional del producto según su ID
            response = requests.get(f'http://127.0.0.1:8000/api/productos/{producto_id}/')
            if response.status_code == 200:
                producto_data = response.json()

                # Actualizar el campo 'nombre' en el diccionario self.carrito
                self.carrito[producto_id]['nombre'] = producto_data['producto'].get('nombre')

                # Agregar el producto actualizado a la lista de productos
                productos.append(self.carrito[producto_id])

        return productos

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.actualizar_total()  # Actualizar el total a pagar
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.idProducto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                del self.carrito[id]
            self.actualizar_total()  # Actualizar el total a pagar
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.actualizar_total()  # Actualizar el total a pagar
        self.session.modified = True

    def actualizar_total(self):
        total = 0
        for item in self.carrito.values():
            total += int(item['acumulado'])

        self.session['total_pagar'] = total
