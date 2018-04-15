import multiprocessing

mode = "wsgi"
working_dir = "/etc/gunicorn.d/"
pythonpath = "/home/box/web/ask"
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count()*2 + 1
timeout = 5
