![pylint score](https://github.com/Kencho/practica-dms-2021-2022/workflows/pylint%20score/badge.svg)
![mypy typechecking](https://github.com/Kencho/practica-dms-2021-2022/workflows/mypy%20typechecking/badge.svg)

# DMS course project codebase, academic year 2021-2022

The goal of this project is to implement a basic online evaluation appliance deployed across several interconnected services.

## Authors

- [Iván Cortés Aliende](https://github.com/ica1006)
- [Alberto Diez Busto](https://github.com/adb1004)
- [Steven Paul Alba Alba](https://github.com/saa1002)

## Instalation manual

Necesitamos descargar el repositorio. Esto se puede hacer desde la web de github o con el comando git clone:
```bash
git clone https://github.com/adb1004/practica-dms-2021-2022
```
Debemos tener en cuenta en qué directorio lo guardaremos, ya que será desde donde ejecutemos el programa.

## Ejecution manual

- Navegar hasta la carpeta donde hicimos el git clone con el comando cd
- Si es la primera vez que lo ejecutamos, deberemos utilizat el comando:
```bash
docker-compose -f docker/config/dev.yml build
```
- Para lanzar los 3 contenedores de docker utilizaremos el comando:
```bash
docker-compose -f docker/config/dev.yml up -d
```
- Cuando queramos parar la ejecución y eliminar los contenedores, utilizaremos el comendo:
```bash
docker-compose -f docker/config/dev.yml rm -sfv 
```
- Podremos ir mirando los logs en tiempo real de cómo se van lanzando con el comando:
```bash
docker logs -f (dms2122backend/dms2122frontend/dms2122auth)
```

## Utilization manual
Una vez lanzado el sistema, podremos ver a que dirección debemos conectarnos desde el navegador mirando el log de dms2122frontend. Si todo ha ido como debería, esa dirección debería ser http://172.10.1.30:8080/login
Las credenciales del administrador por defecto son admin:admin. Con estas credenciales podremos crear nuevos usuarios, asignar roles a estos y editarlos. Los roles que pueden tener los usuarios son administradores, profesores o estudiantes.

### Student
Los estudiantes pueden ver sus preguntas contestadas, ver qué preguntas les quedan por contestar, ver su progresión dentro del curso y contestar a las preguntas pendientes.

### Teacher
Los profesores pueden crear preguntas, editar preguntas (si no han sido ya respondidas), ver una demo de las preguntas, ver estadísticas de sus alumnos y ver estadísticas de las preguntas que este ha creado


## Components

The source code of the components is available under the `components` direcotry.


### Services

The services comprising the appliance are:

#### `dms2122auth`

This is the authentication service. It provides the user credentials, sessions and rights functionalities of the application.

See the `README.md` file for further details on the service.

#### `dms2122backend`

This service provides the evaluation logic (definition of questions, grading, etc.)

See the `README.md` file for further details on the service.

#### `dms2122frontend`

A frontend web service that allows to interact with the other services through a web browser.

See the `README.md` file for further details on the application.

### Libraries

These are auxiliar components shared by several services.

#### `dms2122core`

The shared core functionalities.

See the `README.md` file for further details on the component.

## Docker

The application comes with a pre-configured Docker setup to help with the development and testing (though it can be used as a base for more complex deployments).

To run the application using Docker Compose:

```bash
docker-compose -f docker/config/dev.yml up -d
```

When run for the first time, the required Docker images will be built. Should images be rebuilt, do it with:

```bash
docker-compose -f docker/config/dev.yml build
```

To stop and remove the containers:

```bash
docker-compose -f docker/config/dev.yml rm -sfv
```

By default data will not be persisted across executions. The configuration file `docker/config/dev.yml` can be edited to mount persistent volumes and use them for the persistent data.

To see the output of a container:

```bash
docker logs CONTAINER_NAME
# To keep printing the output as its streamed until interrupted with Ctrl+C:
# docker logs CONTAINER_NAME -f
```

To enter a running service as another subprocess to operate inside through a terminal:

```bash
docker exec -it CONTAINER_NAME /bin/bash
```

To see the status of the different containers:

```bash
docker container ps -a
```

## Helper scripts

The directory `scripts` contain several helper scripts.

- `verify-style.sh`: Runs linting (using pylint) on the components' code. This is used to verify a basic code quality. On GitHub, this CI pass will fail if the overall score falls below 7.00.
- `verify-type-correctness.sh`: Runs mypy to assess the type correctness in the components' code. It is used by GitHub to verify that no typing rules are broken in a commit.
- `verify-commit.sh`: Runs some validations before committing a changeset. Right now enforces type correctness (using `verify-type-correctness.sh`). Can be used as a Git hook to avoid committing a breaking change:
  Append at the end of `.git/hooks/pre-commit`:

  ```bash
  scripts/verify-commit.sh
  ```

## GitHub workflows and badges

This project includes some workflows configured in `.github/workflows`. They will generate the badges seen at the top of this document, so do not forget to update the URLs in this README file if the project is forked!
