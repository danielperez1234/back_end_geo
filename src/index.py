from flask import Flask, render_template
from models import db, MACAddress

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mac_addresses.db'  # Use your preferred database URL
db.init_app(app)

with app.app_context():
    db.create_all()

mac_controller = MACAddressController()

@app.route('/')
def index():
    mac_addresses = MACAddress.query.all()
    return render_template('index.html', mac_addresses=mac_addresses)

if _name_ == '_main_':
    app.run(debug=True)