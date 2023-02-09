from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.ApiHandler import ApiHandler
from waitress import serve

app = Flask(__name__, static_url_path='', \
    static_folder='../client/build',\
        template_folder='../client/build')
mode =''
CORS(app) #comment this on deployment
api = Api(app)
@app.route("/", defaults={'path':''})
def serve(path):
    return render_template('index.html')

api.add_resource(ApiHandler, '/v1/api')

if __name__ == '__main__':
    if mode == "dev":
        app.run(debug=True)
    else:
        serve(app,host="127.0.0.1",port=5000)