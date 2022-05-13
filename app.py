from flask import Flask
from flask_restplus import Api, Resource,reqparse
from flask_cors import CORS

application = Flask(__name__)


API_NAME = Api(application, version="1.0",
               title="BioInformatics",
               default="/",
               default_label="Bioinformatics use cases",
               description="Swagger Documentation",
               strict_slashes=False)
CORS(application)

API_NAME_BI = API_NAME.namespace('BioInformatics ', description= 'End points of BioInformatics use cases')

if __name__ == '__main__':

	app.run(port=8000 ,host='0.0.0.0')
