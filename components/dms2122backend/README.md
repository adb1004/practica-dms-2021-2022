# DMS 2021-2022 Backend Service

This service provides backend logic to the appliance.

## Memoria - Backend

Para poder seguir el principio SOLID de la mejor manera, hemos decidido incorporar las siguientes cuatro capas:
- Base de datos
- Lógica de las preguntas, respuestas y estadísticas
- Servicios
- Capa visible

Mediante la api, en api.yml se pueden ver las diferentes rutas enlazadas a los métodos get, post y put correspondientes a los respectivos servicios, de manera que el frontend se pueda comunicar perfectamente con las capas del backend. Los parámetros utilizados en la capa visible se pasan o mediante la URL o mediante el paquete json correspondiente.

- En la capa de la base de datos se encuentran las clases correspindientes a las tablas de preguntas y respuestas en /data/db. En /data/db/results encontramos las correspondientes clases question y answer con sus tablas y en /data/db/resulsets encontramos en los archivos questions.py y answers.py con los métodos que nos permiten editar estas clases.

- En la capa lógica (presente en /logic) se encuentran las clases LogicQuestion, LogicAnswer y LogicStatistics. Estas clases incorporan los métodos necesarios para comunicarse con la capa de la base de datos y poder trabajar con los datos presentes en esta, como puede ser el cálculo de las estadísticas de preguntas, respuestas y usuarios, así como el lanzamiento de excepciones en caso de algún tipo de error o mal uso de los datos.

- La capa de servicios (/service) contiene una serie de métodos capaces de crear las sesiones en la base de datos para interactuar con la capa lógica y poder almacenar en listas o diccionarios (depende del caso) los resultados optenidos de dicha capa. Trabajando con diccionarios y listas nos es luego mucho más cómodo guardar estos datos en ficheros JSON que podemos transformar en la capa visible fácilmente para ser usados en el frontend.

- Por último, en la capa visible (/presentation) los métodos recogen los datos de la capa de servicios y los transforma para poder ser usados en el frontend directamente. También utilizan las excepciones generadas durante todo el proceso para mostrar mensajes de error de ser necesario (Por ejemplo, en el caso de que al crear una pregunta no se especifique alguno de los datos).

### API Endpoints

#### Answers

 - `/answers`
   - `get`: Devuelve todas las respuestas de la plataforma
 
 - `/answers/{qid}`
   - `get`: Devuelve todas las respuestas a la pregunta especificada por parámetro
   
 - `/answers/{username}`
   - `get`: Devuelve todas las respuestas del usuario especificado por parámetro

#### Questions
 - `/questions`
   - `get`: Devuelve todas las preguntas de la plataforma en un listado
   
 - `/question/create`
   - `post`: Creará una pregunta nueva
   
 - `/question/{qid}`
   - `put`: Modificará la pregunta especificada por parámetro
   - `get`: Devuelve la pregunta especificada por parámetro
   
 - `/question/{qid}/ans`
   - `get`: Devuelve un valor booleano según si la pregunta ha sido respondida por algún alumno
   
 - `/question/{qid}/ans/{username}`
   - `post`: Creará una nueva respuesta a la pregunta especificada por el alumno especificado
   - `get`: Devuelve la respuesta del alumno especificado a la pregunta especificada
   
 - `/questions/{username}/incompleted`
   - `get`: Devuelve todas las preguntas incompletas del usuario especificado por parámetro en un listado
   
 - `/questions/{username}/completed`
   - `get`: Devuelve todas las preguntas completadas del usuario especificado por parámetro en un listado

#### Statistics
 - `/statistics/users`:
   - `get`: Devuelve las estadísticas de todos los usuarios
   
 - `/statistics/{username}`:
   - `get`: Devuelve las estadísticas del alumno especificado por parámetro
   
 - `/statistics/questions`:
   - `get`: Devuelve las estadísticas de todas las preguntas





## Installation

Run `./install.sh` for an automated installation.

To manually install the service:

```bash
# Install the service itself.
./setup.py install
```

## Configuration

Configuration will be loaded from the default user configuration directory, subpath `dms2122backend/config.yml`. This path is thus usually `${HOME}/.config/dms2122backend/config.yml` in most Linux distros.

The configuration file is a YAML dictionary with the following configurable parameters:

- `db_connection_string` (mandatory): The string used by the ORM to connect to the database.
- `host` (mandatory): The service host.
- `port` (mandatory): The service port.
- `debug`: If set to true, the service will run in debug mode.
- `salt`: A configurable string used to further randomize the password hashing. If changed, existing user passwords will be lost.
- `authorized_api_keys`: An array of keys (in string format) that integrated applications should provide to be granted access to certain REST operations.
- `auth_service`: A dictionary with the configuration needed to connect to the authentication service.
  - `host` and `port`: Host and port used to connect to the service.
  - `apikey_secret`: The API key this service will use to present itself to the authentication service in the requests that require so. Must be included in the authentication service `authorized_api_keys` whitelist.

## Running the service

Just run `dms2122backend` as any other program.

## REST API specification

This service exposes a REST API in OpenAPI format that can be browsed at `dms2122backend/openapi/spec.yml` or in the HTTP path `/api/v1/ui/` of the service.

## Services integration

The backend service requires an API key to ensure that only the whitelisted clients can operate through the REST API.

Requesting clients must include their own, unique API key in the `X-ApiKey-Backend` header.

When a request under that security schema receives a request, the key in this header is searched in the whitelisted API keys at the service configuration (in the `authorized_api_keys` entry). If the header is not included or the key is not in the whitelist, the request will be immediately rejected, before being further processed.

This service also has its own API key to integrate itself with the authentication service. This key must be thus whitelisted in the authentication service in order to operate.

As some operations required in the authentication service require a user session, clients using this backend must obtain and keep a valid user session token, that will be passed in the requests to this service to authenticate and authorize them.
