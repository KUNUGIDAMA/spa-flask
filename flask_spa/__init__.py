#flask_spa/__init__.py
from flask import Flask
app=Flask(__name__)
app.config.from_object('flask_spa.config')
app.config['JSON_AS_ASCII']=False
import flask_spa.views
