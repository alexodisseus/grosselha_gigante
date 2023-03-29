import gg.users
import gg.tnp
import gg.admin

from flask import Flask

users = gg.users
tnp = gg.tnp
admin = gg.admin

def create_app():

    app = Flask(__name__)
    app.config['TITLE'] = "Groselha Gigante"

    app.secret_key = b'guerra aos senhores'
    users.configure(app)
    tnp.configure(app)
    admin.configure(app)
    return app


application = create_app()
