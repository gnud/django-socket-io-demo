import os

APP_PORT = os.environ.get('APP_PORT', 8000)
bind = f'0.0.0.0:{APP_PORT}'
workers = os.environ.get('CORE_WORKERS', 2)
threads = os.environ.get('CORE_THREADS', 10)
worker_class = 'gevent'
