# API Flask - Tutorial Javier Pinilla

Este proyecto es una implementación de una API RESTful básica utilizando Python y Flask, basada en el tutorial "Crea Un API Con Python En SOLO 10 MINUTOS" de Javier Pinilla.

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera, con un solo archivo principal `main.py` que contiene toda la lógica de la API.

### Endpoints (Rutas)

*   `GET /`: Ruta principal para verificar que el servidor está en línea. Devuelve `"home"`.
*   `GET /users/<user_id>`: Simula la obtención de un usuario. Permite enviar un parámetro opcional de consulta (`?query=valor`) que se adjunta a la respuesta. Devuelve un JSON simulado con la información del usuario (`id`, `name`, `phone`, `query`).
*   `POST /users`: Recibe información en formato JSON desde el cuerpo de la petición. Retorna esta misma información junto con un campo `status: "user created"` y un código HTTP `201 Created`.

## Requisitos

*   Python 3.x
*   Flask

## Instalación y Ejecución Local

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/JOSTHONS/Resultado-de-implementaci-n-de-la-API-.git
    cd Resultado-de-implementaci-n-de-la-API-
    ```

2.  **Crear y activar un entorno virtual (recomendado):**
    ```bash
    python -m venv .venv
    # En Windows:
    .\.venv\Scripts\Activate.ps1
    # En macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install Flask
    ```

4.  **Ejecutar el servidor:**
    ```bash
    python main.py
    ```
    El servidor se iniciará en modo debug en `http://127.0.0.1:5000/`.

## Pruebas

Puedes probar los endpoints usando herramientas como Postman, cURL o tu navegador web (para las peticiones GET).

*   **Verificar raíz:**
    Abre `http://127.0.0.1:5000/` en tu navegador.
*   **Obtener usuario (GET):**
    Abre `http://127.0.0.1:5000/users/123?query=testing` en tu navegador.
*   **Crear usuario (POST):**
    Usando Postman, envía una petición POST a `http://127.0.0.1:5000/users` con un cuerpo JSON como:
    ```json
    {
        "username": "nuevo_usuario",
        "email": "test@example.com"
    }
    ```
