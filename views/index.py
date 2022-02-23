from flask import Blueprint, render_template, redirect, current_app

index = Blueprint('index', __name__)

@index.route('/')
def index_page():
    return render_template('index.html')

@index.route('/ar')
def invite_page():
    return render_template('main.html')

@index.route('/errors')
def errors_page():
    return render_template('errors.html')