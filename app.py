import psycopg2
from flask import Flask, render_template
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)
app = Flask(__name__)

#@app.route('/hello')
#def hello_world():
#    return "Hello, World!"

@app.route('/home')
def home():
    return render_template('nbatipoff.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
#app.run(host='0.0.0.0', port=105)
