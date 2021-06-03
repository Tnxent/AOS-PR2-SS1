# AOS-PR2
 
subsistema de gestión de clientes de un taller.

# Instalación y uso:

1. Crear una imagen:
```
docker build -t ss1:0.1 .
```

2. Ejecutar la imagen creando un contenedor:
```
docker run -p 8080:8080 ss1:0.1
```

# Guía de uso

### Para ontener todos los clientes:
		GET http://x.x.x.x:8080/clientes
	
### Para registrar un nuevo cliente:
		POST http://x.x.x.x:8080/clientes
		Body:
		{
				"nif/nie": "X9172354-N",
				"idCliente": 452,
				"nombre": "Yunsong",
				"apellidos": "Zhang",
				"domicilio": " Av Gran Vía 100",
				"telefono": "625334697",
				"email": "yszaos@xmail.org"
			}

### Para modificar datos de un cliente identificado por su idCliente:
		PUT http://x.x.x.x:4010/clientes/2021
		headers:
			if-match = 24f21ae791234aeb
		Body:
		{
				"nif/nie": "44917190V",
				"idCliente": 2021,
				"nombre": "Aroa",
				"apellidos": "Luque",
				"domicilio": "C/Amparo, 5",
				"telefono": "687496381",
				"email": "alaos@xmail.org"
			}

### Para obtener datos de un cliente identificado por su idCliente
		GET http://x.x.x.x:8080/clientes/5069
	
### Para obtener datos de un cliente identificado por su NIF o NIE
		GET http://x.x.x.x:8080/clientes/nifnie/28536492-F
 
### Para obtener una lista de aquellos clientes cuyo nombre coincida con el nombre solicitado
		GET http://x.x.x.x:8080/clientes/nombre/Ming
 
