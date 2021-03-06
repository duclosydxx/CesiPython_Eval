from flask import Flask
import json

app = Flask(__name__)
@app.route('/') 
def index():
  return "Hello !"


@app.route('/json') 
def jsonS():
  with open('data.json') as f:
    data = json.load(f)  
  response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
  return response

if __name__ == '__main__':
    app.run(debug=True)

