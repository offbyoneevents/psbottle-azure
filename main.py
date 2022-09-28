import bottle
from bottle import redirect, template, static_file

from mongo import mongo_routes

main_app = bottle.app()

@main_app.get("/")
def index():
    redirect("/mongo")

@main_app.route("/static/<filename>")
@main_app.route("/static/<filename:path>")
def get_static_file(filename):
    return static_file(filename, root="assets")

@main_app.error(404)
def handle_404(error):
    return template("not_found")

@main_app.error(500)
def handle_500(error):
    return template("500_error", error=error)

main_app.merge(mongo_routes)
