  sudo unlink /etc/nginx/sites-enabled/default
  sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
  sudo rm -rf /etc/nginx/sites-enabled/default
  sudo /etc/init.d/nginx restart

  sudo ln -sf /home/box/etc/hello.py /etc/gunicorn.d/hello.py
  sudo ln -sf /home/box/etc/qa.py /etc/gunicorn.d/qa.py
  gunicorn -D -c /etc/gunicorn.d/hello.py hello:app
  gunicorn -D -c /etc/gunicorn.d/qa.py ask.wsgi:application
  
  sudo /etc/init.d/mysql start
  mysql -uroot -e "create database QA"
