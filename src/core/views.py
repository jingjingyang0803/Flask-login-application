from flask import Blueprint, render_template
from flask_login import login_required

from src.utils.decorators import check_is_confirmed

core_bp = Blueprint("core", __name__)

@core_bp.route("/")
@login_required
@check_is_confirmed
def home():
    # url = b"http://testserver.local/#!/login"
    url = "https://www.google.com/"
    return render_template("core/index.html", url=url)