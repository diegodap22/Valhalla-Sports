def importeTotalCarrito(request):
    total=0
    cantidad=0
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            total=total+float(value["precio"])
            cantidad=cantidad+value["cantidad"]
    return {"importeTotalCarrito":total,"cantidadProductos":cantidad}