# flask_blog/views.py
from flask import request,redirect,url_for,render_template,flash,session,jsonify
from flask_spa import app
import json
@app.route('/')
def show_entries():
    return render_template('entries/index.html')


@app.route('/admin')
def admin():
    return render_template('entries/admin.html')