import bottle

from bottle import route, template

@route('/')
def index():
    return '<h1>Hello world from dev!</h1>'

@route('/<name>')
def index(name):
    return template('<h1>Hello from dev {{name}}!</h1>', name=name)

app = application = bottle.default_app()
