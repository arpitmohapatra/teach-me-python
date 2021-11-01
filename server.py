from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '<h1>Flask App</h1>'


@app.errorhandler(404)
def error_page(e):
    print(type(e))
    return '404 error'


app.run()
