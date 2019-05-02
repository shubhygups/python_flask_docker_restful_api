import markdown
import os
import shelve


# Import the framework
from flask import Flask,g
from flask_restful import Resource, Api, reqparse

# Create a instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("employees.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
	"""Present some documentation"""
	
	# Open README file
	with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
		
		# Read the content of the file
		content = markdown_file.read()
		
		# Convert to HTML
		return markdown.markdown(content)
		
class EmployeeList(Resource):
	def get(self):
		shelf = get_db()
		keys = list(shelf.keys())
		 
		employees = []
		 
		for key in keys:
			employees.append(shelf[key])
			
		return {'message': 'Success', 'data': employees}, 200 

	def post(self):
		parser = reqparse.RequestParser()
		
		parser.add_argument('employee_id', required=True)
		parser.add_argument('name', required=True)
		parser.add_argument('age', required=True)
		parser.add_argument('department', required=True)
		parser.add_argument('location', required=True)
		
		# Parse the arguments into a object

		args = parser.parse_args()
		
		shelf = get_db()
		shelf[args['employee_id']] = args
		
		return {'message': 'Employee Registered', 'data':args}, 201

class Employee(Resource):
	
	def get(self, employee_id):
		shelf=get_db()
		
		# If the key doesn't exist in the data store, return 404 error.
		if not (employee_id in shelf):
			return {'mesage': 'Employee not found', 'data': {}}, 404
		
		return {'message': 'Employee found', 'data':shelf[employee_id]}, 200
		
	def delete(self, employee_id):
		shelf=get_db()
		
		# If the key doesn't exist in the data store, return 404 error.
		if not (employee_id in shelf):
			return {'mesage': 'Employee not found', 'data': {}}, 404
		
		del shelf[employee_id]
		return '', 204
				
api.add_resource(EmployeeList, '/employees')		
api.add_resource(Employee, '/employees/<string:employee_id>')