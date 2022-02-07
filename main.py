from flask import Flask,render_template,request,json
import random
import os
import azurebatch

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


# def home():
#     return 'Hello, World!'
@app.route('/')
def base_page():
	return render_template(
		'index.html'  # Template file path, starting from the templates folder. 
	)

# post method for getting folders
@app.route('/submitfolders', methods=(['POST']))
def submitfolders():
  received_data=request.form.to_dict();
  print(received_data)
  # data = {"status": "success"}
  # data.update(received_data)
  # print(data)
  # return data, 200
  response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":received_data}),
        status=200,
        mimetype='application/json')
  return response


@app.route('/monitor')
def monitor():
  return render_template('monitor.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=random.randint(2000, 9000))
  

