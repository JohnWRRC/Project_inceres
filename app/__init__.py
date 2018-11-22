from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__) # instancia que contem tudo do flask
app.config.from_object('config')
db = SQLAlchemy(app) # instancia 
migrate = Migrate(app, db)

manager=Manager(app)
manager.add_command('db',MigrateCommand)

# indicar o caminho completo para importar o modulo
from app.controllers import defualt



