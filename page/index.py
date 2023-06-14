from flask import Blueprint, render_template


index = Blueprint('index', __name__, static_folder='site', template_folder='site')


@index.route('/')
def home():
    return render_template('index.html')