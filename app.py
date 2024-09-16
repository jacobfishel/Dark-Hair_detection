from flask import Flask #initialize app
from views import views

app = Flask(__name__)#initialize this file. This gives us an empty website with nothing.
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, port=8000)

