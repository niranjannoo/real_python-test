# ---- Flask Hello World ---- #
#import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

#error handling
app.config["DEBUG"] =True
# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!!!"

@app.route("/test/<search_Query>")
def search(search_Query):
	return search_Query
@app.route("/integer/<int:value>")
def int_type(value):
	result = value+10
	print(result)
	return "correct and the value is %s"%result
@app.route("/float/<float:value>")
def float_value(value):
	result =value-1.1
	print (result)
	return "correct and the value is %s"%result

@app.route("/url/<path:value>")
def path_type(value):
	print (value)
	return "correct and path is %s"%value

@app.route("/name/<name>")
def index (name):
	if name.lower() == "michael":
		return "Hello, {}",format(name)
	else:
		return "Not Found", 404

# start the development server using the run() method
if __name__ == "__main__":
	app.run()