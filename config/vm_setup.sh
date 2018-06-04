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
sudo pip3 install psycopg2
sudo pip3 install sqlalchemy
sudo pip3 install flask
sudo pip3 install flask-sqlalchemy
sudo pip3 install flask-socketio
sudo pip3 install flask-bcrypt
sudo pip3 install flask-login

mkdir /etc/portals
sudo bash -c "/usr/bin/env python3 /workspace/util/genenv.py > /etc/portals/environment"
sudo ln -s /workspace/config/portals.service /lib/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable portals
sudo systemctl restart portals
