#!/bin/sh
echo "Setting up your environment..."
sudo apt-get update -y
sudo apt-get install python-pip -y
sudo apt-get install postgresql postgresql-contrib -y
sudo apt-get install apache2 -y
sudo apt-get install libapache2-mod-wsgi -y
sudo apt-get build-dep python-psycopg2 -y

echo "Setting up your environment..."

sudo pip install Django==1.5
sudo pip install South==0.8.2
sudo pip install django-tastypie==0.9.12
sudo pip install psycopg2

echo "This may take few minutes..."

su - postgres -c "psql -U postgres -d postgres -c \"Setting user postgres with password 'password';\""

echo "Setting up your database..."

sudo mv /etc/apache2/sites-enabled/000-default.conf /etc/apache2/sites-enabled/000-default.conf.old
sudo mv 000-default.conf /etc/apache2/sites-enabled/
sudo chown www-data:www-data demo/

echo "Restarting apache..."

sudo service apache2 restart

python manage.py syncdb
python manage.py migrate
python manage.py runserver
