# Django with socketio demo

<a href="https://www.buymeacoffee.com/thedudetech"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a pizza&emoji=🍕&slug=thedudetech&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff"></a>

Examples based on [python-socketio](https://github.com/miguelgrinberg/python-socketio/).

# TODO

Changes are work in progress ...

- Port to Django 3.x        [ ]
- Fix timeouts              [ ]
- Fix disconnects           [ ]
- Fix slow view loading     [ ]
- Write tests               [ ]
- Fix Gunicorn / Gevent
   mismatched versions      [ ] 
- Env loader package        [ ]

   
# Quick start

## Development

### pip

```bash
virtualenv -p python3 venv && source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

### run

```bash
./manage.py runserver
```

runserver command has overload in socketio_app
commands to lets Gevent to switch between WSGI request
or WebSocket messages.

## Production

```bash
gunicorn -c gunicorn.cfg.py django_example.wsgi:application
```

- django_example is the project 
- wsgi is wsgi.py module
- application is socketio.WSGIApp wrapper for the Django wsgi application
