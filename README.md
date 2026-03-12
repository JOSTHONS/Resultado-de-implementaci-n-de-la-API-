# 🚀 API Flask - Proyecto de Implementación Exhaustiva

Bienvenido al repositorio oficial del **Proyecto de Implementación de API con Flask**. Este repositorio contiene una API RESTful básica desarrollada en Python, diseñada como un ejercicio fundamental para comprender las bases del desarrollo backend moderno. 

Este proyecto está meticulosamente documentado e inspirado en el tutorial *"Crea Un API Con Python En SOLO 10 MINUTOS"* del canal de YouTube de Javier Pinilla. Hemos expandido los conceptos para entregar una guía completa de aprendizaje.

---

## 📑 Tabla de Contenidos

1. [Acerca del Proyecto](#acerca-del-proyecto)
2. [¿Qué es una API RESTful?](#qué-es-una-api-restful)
3. [¿Por qué Flask y Python?](#por-qué-flask-y-python)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Análisis Profundo del Código (`main.py`)](#análisis-profundo-del-código-mainpy)
6. [Endpoints Disponibles (Documentación de Rutas)](#endpoints-disponibles-documentación-de-rutas)
7. [Requisitos Previos del Sistema](#requisitos-previos-del-sistema)
8. [Guía de Instalación y Despliegue Local](#guía-de-instalación-y-despliegue-local)
9. [¿Qué son y por qué usar Entornos Virtuales?](#qué-son-y-por-qué-usar-entornos-virtuales)
10. [Guía de Pruebas con Postman (Con Evidencia Visual)](#guía-de-pruebas-con-postman-con-evidencia-visual)
11. [Códigos de Estado HTTP Utilizados](#códigos-de-estado-http-utilizados)
12. [Reto de Evidencia y Conclusiones de Aprendizaje](#reto-de-evidencia-y-conclusiones-de-aprendizaje)

---

## 🌟 Acerca del Proyecto

El objetivo principal de esta implementación es asentar los fundamentos del desarrollo de APIs usando el lenguaje de programación Python. A través de este proyecto práctico, no solo se despliega un servidor web funcional, sino que se aborda el manejo del enrutamiento de peticiones HTTP, el procesamiento de parámetros dinámicos, la lectura de cuerpos de solicitud (`body`) en formato JSON y el retorno estructurado de información.

Este repositorio sirve como material de consulta rápida y evidencia del progreso en la ruta de aprendizaje hacia el desarrollo backend avanzado.

---

## 🌐 ¿Qué es una API RESTful?

**API** significa *Application Programming Interface* (Interfaz de Programación de Aplicaciones). Es un conjunto de reglas y mecanismos mediante los cuales una aplicación se comunica con otra.

El término **REST** (*Representational State Transfer*) define un estilo de arquitectura para sistemas hipermedia distribuidos. Una API es "RESTful" cuando se adhiere a las restricciones establecidas por este estilo. Algunas de sus características más importantes incluyen:

*   **Arquitectura Cliente-Servidor:** Separa las preocupaciones de la interfaz de usuario de las preocupaciones de almacenamiento de datos.
*   **Sin Estado (Stateless):** Cada petición del cliente al servidor debe contener toda la información necesaria para comprender y procesar la solicitud. El servidor no guarda contexto entre peticiones.
*   **Interfaz Uniforme:** Se basa en el uso estándar de métodos HTTP (`GET`, `POST`, `PUT`, `DELETE`) para interactuar con los recursos.
*   **Uso de JSON:** Es el formato estándar de la industria para el intercambio de datos entre el cliente (frontend, aplicación móvil, postman) y el servidor (la API).

---

## 🐍 ¿Por qué Flask y Python?

**Python** es uno de los lenguajes de programación más populares y legibles del mundo. Su curva de aprendizaje suave y su inmensa comunidad lo hacen ideal tanto para principiantes como para desarrolladores experimentados.

**Flask** es un "microframework" para Python basado en Werkzeug y Jinja 2. 
Se le llama *micro* porque no requiere herramientas o librerías concretas. No tiene una capa de abstracción de bases de datos, ni validación de formularios, ni otros componentes donde existen librerías de terceros pre-existentes. 

**Ventajas de usar Flask:**
1.  **Simplicidad y Flexibilidad:** A diferencia de frameworks monolíticos como Django, Flask te permite construir exactamente lo que necesitas pieza por pieza.
2.  **Ligereza:** El código base es extremadamente ligero, lo que permite un rápido despliegue y un bajo consumo de recursos.
3.  **Facilidad de Extensibilidad:** A través del vasto ecosistema de extensiones de Flask, puedes agregar funcionalidades como ORMs (SQLAlchemy), autenticación (Flask-Login), y enrutamiento avanzado a medida que tu proyecto crece.

---

## 📂 Estructura del Proyecto

La belleza de este proyecto radica en su simplicidad minimalista. Toda la lógica central reside en el archivo principal de la aplicación.

```text
/Resultado-de-implementaci-n-de-la-API-
│
├── .venv/                      # Directorio del entorno virtual (aislamiento de dependencias)
├── Captura des postman 1.png   # Evidencia: Prueba de endpoint GET (Root)
├── Captura postman 2.png       # Evidencia: Prueba de endpoint GET con parámetros
├── Captura postman 3.png       # Evidencia: Prueba de endpoint POST con JSON
├── main.py                     # Archivo principal que contiene la lógica de la API
└── README.md                   # Este documento de documentación exhaustiva
```

---

## 🔬 Análisis Profundo del Código (`main.py`)

Para entender exactamente qué está sucediendo "bajo el capó", aquí tienes un desglose detallado línea por línea de los componentes principales de nuestro archivo `main.py`:

### 1. Importaciones esenciales
```python
from flask import Flask, jsonify, request
```
*   `Flask`: Es la clase base, nos sirve para instanciar nuestra aplicación web.
*   `jsonify`: Una función utilera que convierte los diccionarios de Python o las listas en objetos de respuesta JSON estructurados y válidos, configurando las cabeceras HTTP correctas (`Content-Type: application/json`).
*   `request`: El objeto global que contiene todos los datos de la petición entrante realizada por el cliente (como parámetros de ruta, variables de consulta y el cuerpo JSON).

### 2. Inicialización
```python
app = Flask(__name__)
```
Instanciamos un objeto de la clase Flask llamado `app`. El argumento `__name__` le indica a Flask dónde buscar los recursos estáticos y plantillas, y mapea la ruta raíz del módulo actual.

### 3. Definiendo Rutas (Endpoints) con Decoradores
Las rutas se definen usando el *decorador* `@app.route()`. Un decorador en Python modifica el comportamiento de una función. En Flask, vincula una URL específica con la función que se define justo debajo.

```python
@app.route("/")
def root():
    ...
```
El bloque de código anterior le dice al servidor: *"Cuando un usuario acceda a la URL raíz (`/`), ejecuta la función `root()`"*.

---

## 🔗 Endpoints Disponibles (Documentación de Rutas)

Nuestra API expone tres rutas principales, cada una con un propósito didáctico específico:

### 1. El Endpoint Raíz (Health Check)
*   **Método HTTP:** `GET`
*   **Ruta:** `/`
*   **Descripción:** Esta ruta sirve como un "Health Check" (Comprobación de salud). Permite saber instantáneamente si el servidor se ha levantado correctamente y está aceptando conexiones.
*   **Respuesta Exitosa:**
    *   **Código:** `200 OK`
    *   **Cuerpo (Texto plano):** `home`

### 2. Obtener Información de un Usuario (Búsqueda por ID)
*   **Método HTTP:** `GET`
*   **Ruta:** `/users/<user_id>`
*   **Parámetros URL Dinámicos:** `<user_id>` (Cadena de texto o número que representa el identificador único del usuario).
*   **Query Parameters (Opcional):** `?query=valor_de_busqueda`
*   **Descripción:** Demuestra cómo capturar valores directamente de la URL. Primero, extrae `<user_id>` de la ruta. Segundo, utiliza `request.args.get("query")` para comprobar si el usuario adjuntó parámetros adicionales tras el símbolo de interrogación `?`.
*   **Ejemplo de Petición:** `http://127.0.0.1:5000/users/456?query=developer`
*   **Respuesta Exitosa:**
    *   **Código:** `200 OK`
    *   **Cuerpo (JSON):**
        ```json
        {
          "id": "456",
          "name": "test",
          "phone": "999666333",
          "query": "developer"
        }
        ```

### 3. Crear un Nuevo Usuario (Recepción de Datos JSON)
*   **Método HTTP:** `POST`
*   **Ruta:** `/users`
*   **Cuerpo Requerido:** JSON válido con la información del usuario.
*   **Descripción:** Esta ruta es el núcleo de las operaciones transaccionales. Al usar explícitamente `methods=["POST"]`, indicamos que esta ruta espera recibir información. Utilizamos `request.json` para extraer el cuerpo de la petición y sumarle metadatos (como la confirmación de estado) antes de devolverlo.
*   **Ejemplo de Petición (Body JSON):**
    ```json
    {
      "username": "josthyn_developer",
      "curso": "Programación Backend",
      "semestre": "Quinto Cuatrimestre"
    }
    ```
*   **Respuesta Exitosa:**
    *   **Código:** `201 Created`
    *   **Cuerpo (JSON):**
        ```json
        {
          "curso": "Programación Backend",
          "semestre": "Quinto Cuatrimestre",
          "status": "user created",
          "username": "josthyn_developer"
        }
        ```

---

## 🛠️ Requisitos Previos del Sistema

Antes de comenzar la instalación, asegúrate de cumplir con los siguientes requisitos en tu ordenador:

1.  **Python 3.7 o superior:** Puedes descargar la versión más reciente desde [python.org](https://www.python.org/downloads/). Recomendamos marcar la casilla *"Add Python to PATH"* durante la instalación en Windows.
2.  **Git:** Para clonar el repositorio. Disponible en [git-scm.com](https://git-scm.com/).
3.  **Terminal/Línea de Comandos:** Windows PowerShell, CMD, Git Bash, o la terminal por defecto en macOS y distribuciones Linux.
4.  **IDE / Editor de Código:** Recomendamos altamente **Visual Studio Code (VS Code)** para explorar y modificar el código.
5.  **Postman (Opcional pero recomendado):** Para realizar las pruebas de funcionalidad. Descargable gratuitamente en [postman.com](https://www.postman.com/downloads/).

---

## 🚀 Guía de Instalación y Despliegue Local

Sigue paso a paso estas instrucciones para poner a correr la API en tu entorno local. 

### Paso 1: Obtener el Código Fuente
Clona el repositorio utilizando tu terminal de comandos e ingresa al directorio recién creado:

```bash
git clone https://github.com/JOSTHONS/Resultado-de-implementaci-n-de-la-API-.git
cd Resultado-de-implementaci-n-de-la-API-
```

### Paso 2: Aislar el Proyecto (Crear Entorno Virtual)
Para no interferir con otras instalaciones de Python en tu sistema, creamos un entorno virtual llamado `.venv`:

```bash
python -m venv .venv
```

### Paso 3: Activar el Entorno Virtual
Dependiendo de tu sistema operativo, el comando de activación varía:

*   **En PowerShell (Windows - Recomendado):**
    ```powershell
    .\.venv\Scripts\Activate.ps1
    ```
*   **En CMD (Símbolo de sistema Windows):**
    ```cmd
    .venv\Scripts\activate.bat
    ```
*   **En macOS y Linux:**
    ```bash
    source .venv/bin/activate
    ```
*(Sabrás que ha funcionado porque el nombre `(.venv)` aparecerá al principio de la línea en tu terminal).*

### Paso 4: Instalar Flask
Con el entorno virtual activado, instalamos el microframework utilizando el gestor de paquetes `pip`:

```bash
pip install Flask
```

### Paso 5: Inicializar el Servidor
Finalmente, ejecutamos nuestro script principal:

```bash
python main.py
```

Deberías ver un mensaje en tu consola indicando que el servidor se está ejecutando en modo desarrollo (debug mode).
> 🟢 **¡Tu API ya está disponible en `http://127.0.0.1:5000/`!**

---

## 🛡️ ¿Qué son y por qué usar Entornos Virtuales?

Al aprender Python, es crítico entender la importancia de los entornos virtuales (`venv`). 

Un entorno virtual es un árbol de directorios autocontenido que aloja una instalación particular de Python junto con un conjunto de librerías de terceros (como Flask en nuestro caso). 

**¿Por qué es indispensable?**
Imagina que tienes el "Proyecto A" que depende de `Flask versión 1.0` y empiezas hoy el "Proyecto B" que necesita `Flask versión 3.0`. Si instalas las librerías de forma global en tu máquina, las versiones colisionarán y uno de tus dos proyectos dejará de funcionar. 
El entorno virtual crea una *burbuja protectora* para que cada proyecto tenga exactamente las dependencias y versiones que necesita de forma completamente aislada del resto de tu computadora.

---

## 🧪 Guía de Pruebas con Postman (Con Evidencia Visual)

Postman es una plataforma estándar en la industria para construir y usar APIs. A continuación, detallamos cómo replicar las pruebas y adjuntamos la evidencia del correcto comportamiento de nuestro desarrollo:

### 1. Comprobando la Disponibilidad del Servidor (Ruta GET `/`)
*   **Acción:** Abre Postman, crea un nuevo "Request", selecciona el método `GET` e ingresa la URL `http://127.0.0.1:5000/`.
*   **Validación:** El servidor recibe la petición y devuelve la palabra "home" indicando que está listo.

![Evidencia de ejecución ruta / (Root)](Captura%20des%20postman%201.png)

### 2. Simulando la Extracción de Datos de Usuario (Ruta GET `/users/<user_id>`)
*   **Acción:** En Postman, utilizando método `GET`, apunta a la URL `http://127.0.0.1:5000/users/1?query=test`.
*   **Validación:** Aquí comprobamos que nuestra API puede interpretar el `1` como el `user_id` e integrarlo en la respuesta. Simultáneamente comprueba la presencia de la variable `query=test` en la URL y añade con éxito el apartado `"query": "test"` dentro del paquete JSON devuelto por el servidor HTTP.

![Evidencia de obtención de parámetros](Captura%20postman%202.png)

### 3. Simulando un Registro en la Base de Datos (Ruta POST `/users`)
*   **Acción:** Configura el método como `POST`. Ingresa la URL `http://127.0.0.1:5000/users`. 
*   **Paso crucial:** En Postman, dirígete a la pestaña **Body**, selecciona la opción **raw** y asegúrate de marcar la casilla desplegable como **JSON** (Mucha atención a este punto, si seleccionas *Text*, Flask rechazará la petición).
*   **Carga el JSON:**
    ```json
    {
        "name": "josthyns"
    }
    ```
*   **Validación:** El servidor Flask procesa el cuerpo, y como se programó en `main.py`, anexa una nueva llave llamada `"status"` con el string `"user created"`. Notar en la captura cómo el Status code es el correcto `201 Created`.

![Evidencia de inyección JSON por POST](Captura%20postman%203.png)

---

## 🚦 Códigos de Estado HTTP Utilizados

Es fundamental comprender qué significan los números devueltos por nuestra API. En este proyecto controlamos dos específicos:

*   🟩 **`200 OK`:** Es la respuesta estándar para peticiones HTTP exitosas. Lo utilizamos en nuestras rutas `GET`. Le indica al cliente (Postman o el navegador) que su solicitud fue recibida, entendida, y que el servidor entregó la información esperada.
*   🟩 **`201 Created`:** Lo utilizamos específicamente en nuestra ruta `POST` (`/users`). Es la forma estandarizada y correcta en el desarrollo de APIs de confirmar que la petición no solo fue exitosa, sino que además *resultó en la creación de un nuevo recurso* en el servidor. 

Conocer y aplicar estos estándares diferencia a un aficionado de un profesional en el ámbito del desarrollo de software backend.

---

## 🎓 Reto de Evidencia y Conclusiones de Aprendizaje

Este repositorio cumple de manera sobrada como evidencia verificable del primer ejercicio práctico de implementación de APIs. 

El repositorio con control de versiones Git puede encontrarse en su versión original y actualizada a través del siguiente enlace oficial: 
👉 **[GitHub Oficial del Proyecto: JOSTHONS](https://github.com/JOSTHONS/Resultado-de-implementaci-n-de-la-API-)**

### 🧠 Lo que aprendí con mis propias palabras

> En este ejercicio aprendí lo fácil y rápido que es levantar un servidor web básico con Python utilizando el framwork Flask. Comprendí cómo definir rutas, cómo manejar diferencias entre peticiones GET y POST, y la importancia de trabajar con formato JSON usando jsonify y request.json para la entrada y salida de datos en una API REST. También aprendí a probar que mi API funcione conectándola con Postman.

---
✨ *Documentación elaborada con dedicación exhaustiva y metodologías ágiles para el desarrollo integral del conocimiento en programación Backend.*
