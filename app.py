# Third-party imports
from flask import Flask, jsonify, request
import json
import connexion
##from decouple import config
from fantasy_app.functions import hello11
from fantasy_app.contest_list import contests


app = connexion.FlaskApp(__name__, specification_dir="./")
app.add_api("swagger.yml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)