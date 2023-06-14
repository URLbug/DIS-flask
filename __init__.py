from flask import Flask


app = Flask(__name__, template_folder='site', static_folder='site')

app.config['SECRET_KEY'] = 'amber'

from page.index import index

app.register_blueprint(index)