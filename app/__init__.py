import os
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key'
)

from app import rutas
from app import api


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)