import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
	return 'Hello World'
	
@app.route('/foo/<name>')
def foo(name):
	return render_template('foo.html', to=name)	

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
#    app.run(debug=True, port=33507)
