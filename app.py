from flask import Flask

# create new Flask instance
app = Flask(__name__)

# define the starting point, aka the root
@app.route('/')

def hello_world():
    return 'Hello world'

