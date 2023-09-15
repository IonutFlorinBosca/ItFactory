from flask import Flask, render_template
from api import tasks

# se creeaza obiectul aplicatiei
app = Flask(__name__)
app.register_blueprint(tasks.bp)


@app.route("/about")
def about():
    return render_template("about.html", info="Ceva important")


@app.route("/")
def index():
    return render_template("index.html")

# ultimul lucru in pagina trebuie sa fie __main__
# aici se porneste aplicatia
if __name__ == '__main__':
    app.run(debug=True)
