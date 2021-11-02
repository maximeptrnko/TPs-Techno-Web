from app import app
from app.model import dict_tasks

from flask import render_template




@app.errorhandler(Exception)
def handle_exception(e):
    return render_template("error_page.html", e=e)


