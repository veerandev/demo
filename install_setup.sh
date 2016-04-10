#!/bin/sh
apt-get update  
apt-get install python-pip -y
apt-get install postgresql postgresql-contrib -y
apt-get install apache2 -y
apt-get install libapache2-mod-wsgi -y
apt-get build-dep python-psycopg2 -y
pip install Django==1.5
pip install South==0.8.2
pip install django-tastypie==0.9.12
pip install psycopg2
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'password';"
mv /etc/apache2/sites-enabled/000-default.conf /etc/apache2/sites-enabled/000-default.conf.old
mv /home/ubuntu/demo/000-default.conf /etc/apache2/sites-enabled/000-default.conf
chown www-data:www-data .
sudo service apache2 restart
python manage.py syncdb
python manage.py migrate
python manage.py runserver
