from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_name():
   return 'Welcome to Flask world'

if __name__ == '__main__':
    app.run(debug=True) 