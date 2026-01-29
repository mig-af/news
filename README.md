
# BoliNews IA (Backend)

Api privada que usa el sitio https://noticias.zetita.online para mostrar resumenes de noticias hechas por IA






## Tech Stack


- Python3.10+
- Flask Framework
- Flask RestFull
- SqlAlchemy
- PyJWT
- MYSQL
- Aiven.io
## Seguridad y Autenticacion

Al ser una API privada los metodos de agregar, eliminar, son extrictamente privados y reestringidos con jwt.
Solo el administrador y el bot tienen acceso a esos metodos 

### Endpoints Principales

####  Obtener todas las noticias de la fecha actual (si no existe, trae la mas reciente guardada en la Db)
```http
    GET /api
```

#### response
```json
[
    {
    "id":1,
    "cuerpo":"Cuerpo de la noticia",
    "url":"https://fuenteDeLaNoticia.com"
    }
]...
```




#### Obtener noticias por fecha 
```http
    GET /api/{fecha}
```

| Parametro | Tipo     |                Descripcion                       |  Reestringido |    
| :-------- | :------- | :-------------------------------- | :--- |
| `fecha`      | `Date` | **Fecha** de la noticia ejem: **2025-11-30** | No




#### Anadir noticias 
```http
    POST /api

```
*Request body json*

| Parametro | Tipo  | Descripcion | Reestringido | 
| :--- | :--- | :--- | :--- |
| `status`| `bool` | Booleano True o False | Si
| `data` | `json` | Cuerpo del contenido ejem: ```{"resumen":[["noticia",["link"]]]}``` | Si

*Ejemplo Body*

```json
    {
        "status":true,
        "data":{
            "resumen":
            [
                ["Noticia resumida",["url de la noticia"]],
                ["Otra Noticia resumida",["url de la otra noticia"]]
            ]
        }
    }
```





#### Eliminar noticias

```http
    DEL /api/{id}

```
| Parametro  | Tipo | Descripcion           | Reestringido |
| :---  | :--- | :--- | :--- |
| `id` | `int` | ID de la noticia | Si |





## Variables de Entorno 

Se debe configurar las siguientes variables de entorno.

`DATABASE_INFO`: Url de conexion a la base de datos

`SECRET_JWT_KEY`: Frase secreta para firmar los tokens



## Instalacion

Instalacion y ejecucion en vercel, despues de ejecutar los pasos importa el proyecto en vercel

* Clona el repositorio
```bash
  git clone https://github.com/mig-af/news
```



* Configura las variables de entorno en vercel
```bash
  DATABASE_INFO=URL_DE_ACCESO_A_TU_DB 
  SECRET_JWT_KEY=FRASE_SECRETA
```

* Configurar administrador
Ingresa a la DB y en la tabla User crear un usuario.
Con ese nombre de usuario y el algoritmo HS256 y tu frase secreta crea tu bearer token en tu plataforma de preferencia, envia el Bearer token en el header de la peticion al hacer post y delete


    
## Notas de implementacion

    Se creo un decorador manual para tener un mejor control del el sistema de autenticacion con pyJwt.  
    Se puede implementar mas reestricciones por ip, dominio, etc 
    Se uso  la capa gratuita de la plataforma aiven.io para alojar la base de datos en dicha plataforma
    

## Autor

- [@MiguelAF](https://www.linkedin.com/in/miguel-ajhuacho-3a55aa350)

