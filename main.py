from flask import Flask, jsonify, request

# Inicialización de la aplicación
app = Flask(__name__)

# Ruta raíz (Root) - Método GET por defecto
@app.route("/")
def root():
    return "home"

# Ruta para obtener un usuario por ID con parámetro de ruta y query
@app.route("/users/<user_id>")
def get_user(user_id):
    # Simulación de datos de usuario
    user = {
        "id": user_id,
        "name": "test",
        "phone": "999666333"
    }
    
    # Obtención de un parámetro de búsqueda (query parameter) opcional
    query = request.args.get("query")
    if query:
        user["query"] = query
        
    return jsonify(user), 200

# Ruta para crear un usuario - Método POST
@app.route("/users", methods=["POST"])
def create_user():
    # Obtener información del cuerpo de la petición (JSON)
    data = request.json
    
    # Simulación de proceso de creación agregando un campo de estatus
    data["status"] = "user created"
    
    # Retornar la información con código 201 (Created)
    return jsonify(data), 201

# Ejecución del servidor en modo de depuración (debug)
if __name__ == "__main__":
    app.run(debug=True)
