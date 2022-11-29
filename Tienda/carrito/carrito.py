

class carrito:
    def __init__(self,request):
        self.request= request
        self.session= request.session
        carrito=self.session.get("carrito")
        if not carrito:
            self.session["carrito"]={}
            self.carrito=self.session["carrito"]
        else:
            self.carrito= carrito
    
    def agregar(self,producto):
        id=str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id":producto.id,
                "nombre":producto.Nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            self.carrito[id]["cantidad"]+=1
            self.carrito[id]["precio"]=self.carrito[id]["cantidad"]*producto.precio
        self.guardarCarrito()
    
    def guardarCarrito(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True

    def eliminar(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardarCarrito()

    def restar(self,producto):
        for key, value in self.carrito.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                if value["cantidad"]==0:
                    self.eliminar(producto)
                break
        self.guardarCarrito()
    
    def limpiarCarrito(self):
        carrito=self.session["carrito"]={}
        self.session.modified=True

        