from helpers import (
    render_template,
    Blueprint,
)

indexBlueprint = Blueprint("index", __name__)


@indexBlueprint.route("/")
def index():
    return render_template("index.html")
