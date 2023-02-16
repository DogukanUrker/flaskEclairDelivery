import socket
from helpers import (
    secrets,
    message,
    render_template,
    Flask,
)

from routes.index import indexBlueprint

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)
app.config["SESSION_PERMANENT"] = True


@app.errorhandler(404)
def notFound(e):
    message("1", "404")
    return render_template("404.html"), 404


app.register_blueprint(indexBlueprint)

match __name__:
    case "__main__":
        app.run(debug=True, host=socket.gethostbyname(socket.gethostname()))
