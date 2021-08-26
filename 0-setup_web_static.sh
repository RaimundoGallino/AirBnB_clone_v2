#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt update -y
sudo apt install nginx -y
mkdir -p /data/web_static/releases/test/
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:user /data/
chown -R ubuntu:group /data/
sed -i "/listen 80 default_server; location /hbnb_static/ { alias /data/web_static/current/; }"
sudo service nginx restart
