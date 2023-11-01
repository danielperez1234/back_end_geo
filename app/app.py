from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configura la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dHb2E5FFc1hB52dDBA5EeGdc3b456b6A@roundhouse.proxy.rlwy.net:18737/railway'
db = SQLAlchemy(app)

# Importar las rutas de usuario
from routes.user import user_bp
from routes.coordinates import coordinate_bp
from routes.style import style_bp

# Registrar las rutas de usuario
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(coordinate_bp, url_prefix='/coordinate')
app.register_blueprint(style_bp, url_prefix='style')

if __name__ == '__main__':
    app.run()
