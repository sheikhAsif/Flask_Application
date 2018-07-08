from flask import Flask,render_template

app_name = Flask(__name__)

@app_name.route("/")
def home():
	name = "Flask Powered Website"
	return render_template('index.html',data=name)
@app_name.route("/hello123/")
def contact():
	d = {
		'name':'Flask',
		'language':'Python',
		'use':'Web Desging',
		'version':0.12,
	}
	return render_template('contact.html',data=d)
@app_name.route('/hello/')
@app_name.route('/hello/<string:name>/')
def hello(name=None):
	return "Welcome User with id {}".format(name)

if __name__ =="__main__":
	app_name.run(host="localhost",port=80,debug=True)