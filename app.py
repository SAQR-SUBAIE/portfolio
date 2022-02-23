from flask import Flask




app = Flask(__name__)

import views

app.register_blueprint(views.index)
app.register_blueprint(views.errors)


if __name__ == '__main__':
    app.run(debug=True, port=3939)