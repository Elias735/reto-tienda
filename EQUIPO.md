# Nuestro equipo

- **Nuestro servicio:** Catálogo · puerto 50051 · contrato `catalogo.proto`
- **Servicio que consumimos (vecino):** Inventario · puerto 50052 · contrato `inventario.proto`
- **Repositorio del equipo vecino:** (https://github.com/Omar050928/Inventario)

| Integrante | Matrícula | Rol |
|---|---|---|
| | | Servidor |
|Diego Verduzco |20205116 | Cliente |
|Elias Vazquez |20206634| Servidor |

| | | Integración (README, issues y prueba cruzada) |

## Prueba cruzada

Corran `python cliente_vecino.py` contra el servidor **real** del equipo vecino (el que clonaron en `../vecino`)
y peguen aquí todo lo que imprimió:

```
=== Parte 1 · ConsultarExistencia con un dato válido ===

Clave: P001 | Cantidad: 5 | Almacén: Colima

=== Parte 2 · ConsultarExistencia con un dato que provoca error ===

Error esperado capturado:
 - Código: StatusCode.NOT_FOUND
 - Detalles: No existe el producto P999

=== Parte 3 · VigilarExistencia (streaming) ===

Clave: P001 | Cantidad: 5 | Almacén: Colima
Clave: P001 | Cantidad: 4 | Almacén: Colima
Clave: P001 | Cantidad: 3 | Almacén: Colima
Clave: P001 | Cantidad: 2 | Almacén: Colima
```

## Issues

Enlaces a los issues que abrieron en el repositorio del vecino o que les abrieron a ustedes (si hubo):

-

## Uso de IA (Acuerdo No. 23/2024 UdeC)

Se utiizo el agente de visual studio (copilot) para coreccion y revision de cada linea del servidor 

-
