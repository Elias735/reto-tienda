# Servidor del servicio Catálogo · Reto de integración · Unidad II
# Contrato: catalogo.proto · Puerto: 50051
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures

import catalogo_pb2
import catalogo_pb2_grpc

# Datos de ejemplo (no hace falta base de datos)
PRODUCTOS = {
    "P001": ("Laptop 14 pulgadas", 1299900, "computo"),
    "P002": ("Mouse inalambrico", 29900, "accesorios"),
    "P003": ("Audifonos bluetooth", 89900, "audio"),
    "P004": ("Teclado mecanico", 119900, "accesorios"),
    "P005": ("Bocina portatil", 69900, "audio"),
    "P006": ("Monitor 24 pulgadas", 329900, "computo"),
}


class CatalogoServicio(catalogo_pb2_grpc.CatalogoServicer):

    def ObtenerProducto(self, request, context):
        clave = request.clave

        # Validar el formato de la clave
        if not re.fullmatch(r"P\d{3}", clave):
            context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "Formato de clave: P y 3 dígitos",
            )

        # Buscar el producto
        producto = PRODUCTOS.get(clave)

        # Verificar si existe
        if producto is None:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"No existe el producto {clave}",
            )

        # Extraer los datos del producto
        nombre, precio_centavos, categoria = producto

        # Regresar un solo producto
        return catalogo_pb2.Producto(
            clave=clave,
            nombre=nombre,
            precio_centavos=precio_centavos,
            categoria=categoria,
    )
    def ListarCategoria(self, request, context):
        # STREAMING: entrega VARIAS cajas con yield
        # TODO
        
        # Si request.categoria viene vacía: context.abort(grpc.StatusCode.INVALID_ARGUMENT, ...)
        # Si ningún producto tiene esa categoría: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si hay: por cada producto de esa categoría, espera 0.5 s y haz yield de un catalogo_pb2.Producto.
        if not request.categoria:
            context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "La categoría no puede estar vacía",
            )

        productos = [
            (clave, nombre, precio_centavos, categoria)
            for clave, (nombre, precio_centavos, categoria) in PRODUCTOS.items()
            if categoria == request.categoria
        ]
        if not productos:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"No existen productos de la categoría {request.categoria}",
            )

        for clave, nombre, precio_centavos, categoria in productos:
            time.sleep(0.5)
            yield catalogo_pb2.Producto(
                clave=clave,
                nombre=nombre,
                precio_centavos=precio_centavos,
                categoria=categoria,
            )


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
catalogo_pb2_grpc.add_CatalogoServicer_to_server(CatalogoServicio(), servidor)
servidor.add_insecure_port("[::]:50051")
servidor.start()
print("Servidor de Catálogo escuchando en el puerto 50051...")
servidor.wait_for_termination()
