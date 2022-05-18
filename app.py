from flask import Flask

from flask_restful import Resource, Api

app = Flask(__name__)


app.config['SECRET_KEY'] = 'disable the web security'
app.config['CORS_HEADERS'] = 'Content-Type'
API_NAME = Api(app,
               version="1.0",
               title="vLife Demo App",
               default=None,
               default_label=None,
               description="Swagger Documentation of Demo app",
               strict_slashes=False)


class Helloworld(Resource):

	def __init__(self):

		pass

	def get(self):

		return {

			"Hello": "World-:)"

		}

API_NAME = API_NAME.namespace('vLifeHealthMonitor', description= "API's for health monitor dashboard")
	
API_NAME.add_resource(Helloworld, '/')

if __name__ == '__main__':

	app.run(debug=True)
