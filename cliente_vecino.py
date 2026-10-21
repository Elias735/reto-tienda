# Cliente del servicio Inventario (equipo vecino) · Reto de integración
# Contrato del vecino: inventario.proto · Qué hace y con qué datos probar: servicios/inventario/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc

import inventario_pb2
import inventario_pb2_grpc

canal = grpc.insecure_channel("localhost:50052")
stub = inventario_pb2_grpc.InventarioStub(canal)

print("\n=== Parte 1 · ConsultarExistencia con un dato válido ===\n")
# TODO: arma la petición con un dato que funcione (tabla "Datos para probar" del README del vecino),
#       llama a stub.ConsultarExistencia(...) e imprime los campos de la respuesta.
peticion_valida = inventario_pb2.ExistenciaRequest(clave="P001")
respuesta = stub.ConsultarExistencia(peticion_valida)
print(
    f"Clave: {respuesta.clave} | "
    f"Cantidad: {respuesta.cantidad} | "
    f"Almacén: {respuesta.almacen}"
)

print("\n=== Parte 2 · ConsultarExistencia con un dato que provoca error ===\n")
# TODO: llama con un dato que provoque error, dentro de try/except grpc.RpcError,
#       e imprime e.code() y e.details(). El programa NO debe tronar.
peticion_error = inventario_pb2.ExistenciaRequest(clave="ABC")
try:
    stub.ConsultarExistencia(peticion_error)
except grpc.RpcError as e:
    print("Error esperado capturado:")
    print(f" - Código: {e.code()}")
    print(f" - Detalles: {e.details()}")

print("\n=== Parte 3 · VigilarExistencia (streaming) ===\n")
# TODO: recorre stub.VigilarExistencia(...) con for e imprime cada caja en cuanto llegue.
#       Ponlo también dentro de try/except por si el servidor regresa un error.
peticion_invalida = inventario_pb2.ExistenciaRequest(clave="P999")
try:
    for actualizacion in stub.VigilarExistencia(peticion_invalida):
        print(
            f"Clave: {actualizacion.clave} | "
            f"Cantidad: {actualizacion.cantidad} | "
            f"Almacén: {actualizacion.almacen}"
        )
except grpc.RpcError as e:
    print("El stream se interrumpió o devolvió un error:")
    print(f" - Código: {e.code()}")
    print(f" - Detalles: {e.details()}")
