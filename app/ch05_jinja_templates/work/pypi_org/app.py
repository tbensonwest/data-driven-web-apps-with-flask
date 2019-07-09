import flask
from pypi_org.infrastructure.view_modifiers import response

app = flask.Flask(__name__)

def get_latest_packages():
    return [
        {'name': 'flask', 'version': '1.2.3'},
        {'name': 'sqlalchemy', 'version': '2.2.0'},
        {'name': 'passlib', 'version': '3.0.0'},
    ]

@app.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = get_latest_packages()
    return {'packages': test_packages}

@app.route('/about')
@response(template_file='home/about.html')
def about():
    return {}

if __name__ == '__main__':
    app.run(debug=True)