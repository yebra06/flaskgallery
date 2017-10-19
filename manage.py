from flask import Flask, render_template
from flask_assets import Environment, Bundle


# Configure app.
app = Flask(__name__)
app.config.from_object('config.DevConfig')

# Compile style assets.
assets = Environment(app)
scss = Bundle('scss/base.scss', filters='pyscss', output='css/all.css')
assets.register('scss_all', scss)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
