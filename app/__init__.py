from flask import Flask

app = Flask(__name__)

from app.main import main

app.register_blueprint(main)

