from flask import Flask
from dotenv import load_dotenv
from controller.metadata import Metadata
import os 
import logging

 
logging.basicConfig(filename = 'logs/flask.log', level=logging.INFO, format='[%(asctime)s] %(levelname)s %(name)s : %(message)s')

app = Flask(__name__)

@app.route("/")
def homepage():
    metadata= Metadata()
    return metadata.print_hello_world()


if __name__=="__main__":
    load_dotenv() # Load .env variables
    app.run(host=os.environ.get("HOST_URL"), port=os.environ.get("HOST_PORT"), debug=True)