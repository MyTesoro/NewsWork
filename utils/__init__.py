import os
from flask import Flask


def create_app():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')
    app = Flask(__name__, static_folder=static_dir, template_folder=templates_dir)
    return app
