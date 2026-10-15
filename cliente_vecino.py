# Cliente del servicio Inventario (equipo vecino) · Reto de integración
# Contrato del vecino: inventario.proto · Qué hace y con qué datos probar: servicios/inventario/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc

import inventario_pb2
import inventario_pb2_grpc

canal = grpc.insecure_channel("localhost:50052")
stub = inventario_pb2_grpc.InventarioStub(canal)

print("=== Parte 1 · ConsultarExistencia con un dato válido ===")
# TODO: arma la petición con un dato que funcione (tabla "Datos para probar" del README del vecino),
#       llama a stub.ConsultarExistencia(...) e imprime los campos de la respuesta.

print("=== Parte 2 · ConsultarExistencia con un dato que provoca error ===")
# TODO: llama con un dato que provoque error, dentro de try/except grpc.RpcError,
#       e imprime e.code() y e.details(). El programa NO debe tronar.

print("=== Parte 3 · VigilarExistencia (streaming) ===")
# TODO: recorre stub.VigilarExistencia(...) con for e imprime cada caja en cuanto llegue.
#       Ponlo también dentro de try/except por si el servidor regresa un error.
