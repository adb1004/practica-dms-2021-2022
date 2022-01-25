# DMS 2021-2022 Frontend service

This frontend serves as the human interface for the other services of the appliance.

## Memoria - Frontend

Todos los ficheros HTML incorporados por nosotros se encuentran dentro de la carpeta /templates. A su vez, todo lo relativo a los estilos se encuentra en el fichero css /static/styles.css

Ficheros implementados:
  - `sProgression.html`: Muestra el progreso del estudiante. Bloques utilizados: contentsubheading, studentcontent y progressioncontent
  - `sQuestions.html`: Muestra el panel relativo a las preguntas de los estudiantes. Bloques utilizados: contentsubheading, studentcontent y squestioncontent
  - `sQuestionsCompleted-Display.html`: Muestra la pregunta en cuestión respondida por el estudiante. Bloques utilizados: contentsubheading, studentcontent, squestioncontent, squestioncompletedcontent y displaycontent
  - `sQuestionsCompleted.html`: Muestra las preguntas respondidas por el estudiante. Bloques utilizados: contentsubheading, studentcontent, squestioncontent, squestioncompletedcontent.
  - `sQuestionsIncompleted-Complete.html`: Muestra la plantilla para responder a una pregunta en cuestión. Bloques utilizados: contentsubheading, studentcontent, squestioncontent, squestionincompletedcontent y completecontent.
  - `sQuestionsIncompleted.html`: Muestra las preguntas no respondidas por el estudiante. Bloques utilizados: contentsubheading, studentcontent, squestioncontent y squestionincompletedcontent.
  - `tQuestions.html`: Muestra el panel relativo al manejo de preguntas desde la parte del profesor. Bloques utilizados: contentsubheading, teachercontent, tquestioncontent.
  - `tQuestionsCreate.html`: Muestra el panel para la creación de preguntas. Bloques utilizados: contentsubheading, teachercontent, tquestioncontent y tquestioncreatecontent.
  - `tQuestionsDisplay.html`: Muestra la "demo" de una pregunta en cuestión como si fuera la perspectiva de un alumno. Bloques utilizados: contentsubheading, teachercontent, tquestioncontent y tquestiondisplaycontent.
  - `tQuestionsModify.html`: Muestra el panel de edición de una pregunta. Bloques utilizados contentsubheading, teachercontent, tquestioncontent y tquestionmodifycontent.
  - `tQuestionsProgressions.html`: Muestra las estadísticas relativas a las distintas preguntas. Bloques utilizados: contentsubheading, teachercontent y questionprogressioncontent
  - `tStudents.html`: Muestra las estadísticas de los distintos estudiantes en cuanto a las preguntas. Bloques utilizados: contentsubheading, teachercontent y tstudentcontent



### Endpoints

  Estos se encuentran declarados en /bin/dms2122frontend y cada uno llamará a su respectivo semejante de la capa visible. En concreto son:
  - /dms2122frontend/presentation/web/`adminendpoints.py`
  - /dms2122frontend//presentation/web/`commonendpoints.py`
  - /dms2122frontend//presentation/web/`sessionendpoints.py`
  - /dms2122frontend//presentation/web/`studentendpoints.py`
  - /dms2122frontend//presentation/web/`teacherendpoints.py`
  
  Al estar divididos los endpoints de esta manera conseguimos que los principios de Interface Segregation y Single Responsibility se cumplan.
  
### Comunicación Frontend - Backend
  Para la comunicación desde el frontend al backend existe una clase de la capa de datos llamada `BackendService` que realiza llamadas a los distintos métodos a traves de los endpoints de la API. En la capa visible de presentación se han implementado las clases `WebAnswer`, `WebQuestion` y `WebStatistics` que realizan cada una sus respectivas operaciónes a través del backend. Estas son las clases utilizadas desde los endpoints una vez sus métodos son llamados al acceder a una de las páginas.



## Installation

Run `./install.sh` for an automated installation.

To manually install the service:

```bash
# Install the service itself.
./setup.py install
```

## Configuration

Configuration will be loaded from the default user configuration directory, subpath `dms2122frontend/config.yml`. This path is thus usually `${HOME}/.config/dms2122frontend/config.yml` in most Linux distros.

The configuration file is a YAML dictionary with the following configurable parameters:

- `service_host` (mandatory): The service host.
- `service_port` (mandatory): The service port.
- `debug`: If set to true, the service will run in debug mode.
- `app_secret_key`: A secret used to sign the session cookies.
- `auth_service`: A dictionary with the configuration needed to connect to the authentication service.
  - `host` and `port`: Host and port used to connect to the service.
- `backend_service`: A dictionary with the configuration needed to connect to the backend service.
  - `host` and `port`: Host and port used to connect to the service.

## Running the service

Just run `dms2122frontend` as any other program.

## Services integration

The frontend service is integrated with both the backend and the authentication services. To do so it uses two different API keys (each must be whitelisted in its corresponding service); it is a bad practice to use the same key for different services, as those with access to the whitelist in one can create impostor clients to operate on the other.

## Authentication workflow

Most, if not all operations, require a user session as an authorization mechanism.

Users through this frontend must first log in with their credentials. If they are accepted by the authorization service, a user session token will be generated and returned to the frontend. The frontend will then store the token, encrypted and signed, as a session cookie.

Most of the interactions with the frontend check and refresh this token, so as long as the service is used, the session will be kept open.

If the frontend is kept idle for a long period of time, the session is closed (via a logout), or the token is lost with the cookie (e.g., closing the web browser) the session will be lost and the cycle must start again with a login.

## UI pages and components

The UI has the following templates hierarchy and structure:

- `base.html`: Base page. Blocks defined: `title`, `pagecontent`, `footer`.
  - `login.html`: Login form page. Macros used: `flashedmessages`, `submit_button`.
  - `base_logged_in.html`: Base page when a user is logged in. Blocks used: `pagecontent`. Blocks defined: `contentheading`, `contentsubheading`, `maincontent`. Macros used: `flashedmessages`, `navbar`.
    - `home.html`: Home page/dashboard. Blocks used: `title`, `contentheading`, `maincontent`.
    - `student.html`: Main student panel. Blocks used: `title`, `contentheading`, `maincontent`. Blocks defined: `subtitle`, `studentcontent`.
    - `teacher.html`: Main teacher panel. Blocks used: `title`, `contentheading`, `maincontent`. Blocks defined: `subtitle`, `teachercontent`.
    - `admin.html`: Main administration panel. Blocks used: `title`, `contentheading`, `maincontent`. Blocks defined: `subtitle`, `administrationcontent`.
    - `admin/users.html`: Users administration listing. Blocks used: `contentsubheading`, `administrationcontent`. Macros used: `button`.
    - `admin/users/new.html`: User creation form page. Blocks used: `contentsubheading`, `administrationcontent`. Macros used: `button`, `submit_button`.
    - `admin/users/edit.html`: User editing form page. Blocks used: `contentsubheading`, `administrationcontent`. Macros used: `button`, `submit_button`.

The following macros/components are provided:

- `macros/navbar.html`
  - `navbar(roles)`: The top navigation bar.
    - Parameters:
      - `roles`: A list of role names.
- `macros/flashedmessages.html`
  - `flashedmessages()`: The bottom panel with the flashed messages.
- `macros/buttons.html`
  - `button(color_class, href, content, onclick=None)`: A link with the appearance of a button.
    - Parameters:
      - `color_class`: A string with a CSS class to use to colorize it (e.g., `bluebg`, `redbg`, `yellowbg`)
      - `href`: The link to follow when clicked.
      - `content`: The contents (usually a string) to display inside the button.
      - `onclick`: If provided, a JavaScript snippet to be run when clicked.
  - `submit_button(color_class, content)`: Special button that submits the containing form. Uses the `button` macro providing a blank link `'#'` as the `href` and a form-submitting statement as the `onclick` argument.
    - Parameters:
      - `color_class` (See `button`)
      - `content` (See `button`)
