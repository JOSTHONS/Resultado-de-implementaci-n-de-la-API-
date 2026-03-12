# 🚀 API Flask - Proyecto de Implementación

Este repositorio contiene una implementación de una API RESTful básica desarrollada en Python utilizando el microframework Flask. El proyecto está basado en el tutorial *"Crea Un API Con Python En SOLO 10 MINUTOS"* del canal de YouTube de Javier Pinilla.

---

## 📂 Estructura del Proyecto

El código está diseñado para ser simple y directo. Toda la lógica de la aplicación se encuentra en un único archivo principal:

- `main.py`: Contiene la configuración de Flask y la definición de las rutas (endpoints) de la API.

---

## 🔗 Endpoints Disponibles

La API cuenta con las siguientes rutas funcionales:

*   🟢 `GET /`: Ruta principal que verifica si el servidor está en funcionamiento. Retorna un mensaje indicando que estás en el `"home"`.
*   🔍 `GET /users/<user_id>`: Simula la consulta de los datos de un usuario específico mediante su ID. También permite el uso de parámetros de consulta u opcionales (por ejemplo, `?query=valor`). La respuesta es un JSON que contiene `id`, `name`, `phone` y el valor del `query`.
*   ➕ `POST /users`: Ruta utilizada para registrar nueva información. Recibe un payload en formato JSON y devuelve esos mismos datos de confirmación junto con un estado `status: "user created"` y código HTTP `201 Created`.

---

## 🛠️ Requisitos del Sistema

Para ejecutar este proyecto en tu entorno local, necesitas tener instalado:

- Python 3.x
- Flask

---

## 🚀 Instalación y Despliegue Local

Sigue estos pasos para probar la API en tu propia computadora:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/JOSTHONS/Resultado-de-implementaci-n-de-la-API-.git
   cd Resultado-de-implementaci-n-de-la-API-
   ```

2. **Crea y activa un entorno virtual (muy recomendado):**
   ```bash
   python -m venv .venv
   
   # Para usuarios de Windows:
   .\.venv\Scripts\Activate.ps1
   
   # Para usuarios de macOS/Linux:
   source .venv/bin/activate
   ```

3. **Instala las dependencias necesarias:**
   ```bash
   pip install Flask
   ```

4. **Inicia el servidor local:**
   ```bash
   python main.py
   ```
   > 💡 El servidor se ejecutará en modo debug y estará disponible en: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🧪 Pruebas con Postman

Puedes interactuar con los endpoints utilizando herramientas como Postman. A continuación se presentan las capturas de evidencia del funcionamiento de la API:

### 1. Verificando la ruta principal (GET)
*Al acceder al home se confirma que el servidor está respondiendo adecuadamente.*

![Captura de la ruta principal](Captura%20des%20postman%201.png)

### 2. Probando la obtención de un usuario (GET)
*Se envía el user_id y un query. La API los procesa y responde correctamente.*

![Captura de consulta de usuario](Captura%20postman%202.png)

### 3. Creación de un usuario (POST)
*Se envía un cuerpo (Body) en formato JSON, y la API contesta con el status `201 Created`.*

![Captura de creación de usuario](Captura%20postman%203.png)

---

## 📚 Reto de Evidencia y Aprendizaje

Este repositorio cumple como evidencia del primer ejercicio práctico de implementación de APIs.
Puedes encontrar el código hospedado en: [GitHub - JOSTHONS](https://github.com/JOSTHONS/Resultado-de-implementaci-n-de-la-API-)

### 🧠 Comentario de Aprendizaje

> *"Durante el desarrollo de este ejercicio, descubrí lo rápido y directo que resulta levantar un servidor web básico en Python usando Flask. Comprendí el uso de los decoradores (`@app.route`) para definir endpoints, aprendí a diferenciar la lógica y comportamiento entre peticiones `GET` y `POST`, y reforcé mis conocimientos sobre el manejo de estructuras JSON (`jsonify` y `request.json`) para el intercambio de datos. Adicionalmente, practicar directamente con Postman me permitió consolidar mis habilidades para probar y verificar el funcionamiento de desarrollo backend."*

---
✨ *Desarrollado y documentado con dedicación.*
