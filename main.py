from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ATIVIDADE_FLASK'

from controllers.ProblemaController import *
from controllers.AutorController import *


if __name__ == "__main__":
    app.run(debug=True, port=5002)
