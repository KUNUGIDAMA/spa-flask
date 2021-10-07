# flask_blog/views.py
import os
from flask import request,redirect,url_for,render_template,flash,session,jsonify,send_from_directory
from flask_spa import app
import json
@app.route('/')
def show_entries():
    return render_template('entries/index.html')


@app.route('/admin')
def admin():
    return render_template('entries/admin.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')