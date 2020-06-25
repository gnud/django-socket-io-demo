# Django with socketio demo

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