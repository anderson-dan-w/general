#!/usr/bin/python3.3
from bottle import debug, get, post, request, route, run
from bottle import jinja2_template as template
from bottle import jinja2_view as view

## my modules
from hlp import getHLP

@route("/hello")
@route("/hello/<name>")
#@view("base")
def hello(name=None):
    return template('home.tpl', name=name)

@get("/login")  ## or @route("/login")  - seems GET is default
def login():
    return '''
        <form action="/login" method="post">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
        </form>
    '''

@post("/login") ## or @route("/login", method="POST")
def do_login():
    user = request.forms.get("username")
    pswd = request.forms.get("password")
    if user == pswd:
        return "<p>don't make your password your username... idiot</p>"
    else:
        return "<p>username and password are different... maybe valid?</p>"

@get("/hlp")
def hlp():
    return template('hlp.tpl', hls=getHLP.getHLP())

debug(True)
run(host="localhost", port=8080)


