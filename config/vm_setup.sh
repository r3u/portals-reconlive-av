#!/bin/bash

set -eu

export DEBIAN_FRONTEND=noninteractive

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install vim
sudo apt-get -y install postgresql
sudo apt-get -y install gunicorn3
sudo apt-get -y install ipython3
sudo apt-get -y install python3-pip

sudo pip3 install eventlet
sudo pip3 install psycopg2-binary
sudo pip3 install sqlalchemy
sudo pip3 install flask
sudo pip3 install flask-sqlalchemy
sudo pip3 install flask-socketio
sudo pip3 install flask-bcrypt
sudo pip3 install flask-login

sudo useradd -M portals --shell /bin/false
sudo usermod -L portals

mkdir /etc/portals
sudo bash -c "/usr/bin/env python3 /workspace/util/genenv.py > /etc/portals/environment"
sudo ln -s /workspace/config/portals.service /lib/systemd/system/

sudo -u postgres createdb portals
echo 'CREATE EXTENSION IF NOT EXISTS "uuid-ossp";' | sudo -u postgres psql
echo "CREATE ROLE portals LOGIN PASSWORD 'portals' NOINHERIT NOCREATEDB;" | sudo -u postgres psql portals
echo 'CREATE SCHEMA portals AUTHORIZATION portals;' | sudo -u postgres psql portals
sudo -u portals psql < /workspace/schema/portals.sql

sudo systemctl daemon-reload
sudo systemctl enable portals
sudo systemctl restart portals
