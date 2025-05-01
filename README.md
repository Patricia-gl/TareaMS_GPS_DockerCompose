# TAREA MICROSERVICIOS DOCKER

## ----Ejecución----
Estando en la ubicación del proyecto y con docker desktop abierto

Comando para levantar los microserivicios:

```"docker compose up -d --build"```

## ----Rutas disponibles----

### Estudiantes

#### GET

Listar estudiantes:

`http://localhost:3000/estudiantes`

Obtener estudiante por rut:

`http://localhost:3000/estudiantes/<rut>`

`http://localhost:3000/estudiantes/11222333-4`


#### POST

Crear estudiante:

`http://localhost:3000/estudiantes`

Ejemplo de JSON:

```json
{
    "rut":"11222333-4",
    "nombre": "Prueba",
    "edad":20,
    "curso": "1ro"
}
```

### Evaluaciones

#### GET

Listar evaluaciones:

`http://localhost:3001/evaluacion`

Obtener evaluaciones por rut:

`http://localhost:3001/evaluacion/<rut>`

`http://localhost:3001/evaluacion/11222333-4`

#### POST

Crear evaluacion:

`http://localhost:3001/evaluacion`

```json
{
    "asignatura": "fisica",
    "nota": 5.4,
    "rut": "11222333-4",
    "semestre": "2"
}
```