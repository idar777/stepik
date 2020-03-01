sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo cp /home/box/web/hello.py /home/box/
sudo gunicorn -b 0.0.0.0:8080 hello:application &
sudo /etc/init.d/nginx restart
