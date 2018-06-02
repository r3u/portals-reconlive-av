#!/bin/bash

set -eu

export DEBIAN_FRONTEND=noninteractive

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install vim
sudo apt-get -y install postgresql
sudo apt-get -y install gunicorn3
sudo apt-get -y install ipython3
sudo apt-get -y install python3-flask
sudo apt-get -y install python3-psycopg2
sudo apt-get -y install python3-sqlalchemy
sudo apt-get -y install python3-eventlet

sudo apt-get -y install python3-pip

sudo pip3 install flask-socketio

sudo ln -s /workspace/config/portals.service /lib/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable portals
sudo systemctl restart portals
