from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

# create a simple route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def admin():
    return render_template('home.html')
