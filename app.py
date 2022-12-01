from flask import Flask, render_template
from db import mysql
from routes.routes import routes


app = Flask(__name__)

app.add_url_rule(routes["index_route"],view_func=routes["indexcontroller"])

app.add_url_rule(routes["quemsomos_route"],view_func=routes["quemsomos_controller"])

app.add_url_rule(routes["contato_route"],view_func=routes["contato_controller"])

app.add_url_rule(routes["envio_route"],view_func=routes["envio_controller"])
