from flask import Flask, request, send_file
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/getcs", methods=['GET'])
def serve_nflu_js():
	return send_file('styles.css', mimetype='text/css')
