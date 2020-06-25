# Django with socketio demo

Examples based on [python-socketio](https://github.com/miguelgrinberg/python-socketio/).

# TODO

Changes are work in progress ...

- Port to Django 3.x        [ ]
- Fix timeouts              [ ]
- Fix disconnects           [ ]
- Fix slow view loading     [ ]
- Write tests               [ ]
- Fix gunicorn/gevent
   mismatched versions      [ ] 
- Env loader package        [ ]

   
# Quick start

## Development

```python
./manage.py runserver
```

runserver commange has overload in socketio_app
commands to lets gevent to switch between WSGI request
or WebSocket messages.

## Production

```python
gunicorn -c gunicorn.cfg.py django_example.wsgi:application
```

- django_example is the project 
- wsgi is wsgi.py module
- application is socketio.WSGIApp wrapper for the Django wsgi application