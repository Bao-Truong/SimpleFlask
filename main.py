from flask import Flask
from dotenv import load_dotenv
from controller.metadata import Metadata
from util.secrets import secretGenerator
import os 
import logging

 
logging.basicConfig(filename = 'logs/flask.log', level=logging.INFO, format='[%(asctime)s] %(levelname)s %(name)s : %(message)s')

app = Flask(__name__)

@app.route("/")
def homepage():
    metadata= Metadata()
    return metadata.print_hello_world()

@app.route("/secret")
def secretToken():
    sg=secretGenerator()
    return sg.getRandomHexSecret()

@app.route("/secretstring")
def secretstring():
    sg=secretGenerator()
    return sg.getRandomString()

@app.route("/secretnumber")
def secretnumber():
    sg=secretGenerator()
    return str(sg.getRandomInt())


if __name__=="__main__":
    load_dotenv() # Load .env variables
    app.run(host=os.environ.get("HOST_URL"), port=os.environ.get("HOST_PORT"))