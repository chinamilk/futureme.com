#!/usr/bin/env python
import bottle

bottle.debug(True)

route = bottle.route
template = bottle.template

@route('/')
def index():
    return template('index')

@route('/about')
def about():
    return template('about')

@route('/contact')
def contact():
    return template('contact')

@route('/wizard')
def wizard():
    return template('wizard')

@route('/education')
def education():
    return template('education')

@route('/salt_smart')
def salt_smart():
    return template('salt_smart')

@route('/salt_smart_answer')
def salt_smart_answer():
    return template('salt_smart_answer')

@route('/chart', method = 'POST')
def chart():
    request = bottle.request
    first_name = request.forms.get('firstName')
    last_name = request.forms.get('lastName')
    return template('chart', 
                    first_name = first_name,
                    last_name = last_name,
                    )

@route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='./static')

bottle.run(host='localhost', port=8080, reloader=True)
