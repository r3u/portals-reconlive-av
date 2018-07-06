#!/bin/bash

set -euo pipefail

export DEBIAN_FRONTEND=noninteractive

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install libcap2-bin
sudo apt-get -y install vim
sudo apt-get -y install postgresql
sudo apt-get -y install ipython3
sudo apt-get -y install python3-pip

sudo pip3 install -r /workspace/requirements.txt

sudo setcap 'cap_net_bind_service=+ep' $(readlink -f $(which python3))

sudo useradd -M portals --shell /bin/false
sudo usermod -L portals

sudo mkdir -p /var/lib/portals/uploads
sudo chown -R portals:portals /var/lib/portals
sudo mkdir /etc/portals
sudo bash -c "/usr/bin/env python3 /workspace/util/genenv.py > /etc/portals/environment"
sudo ln -s /workspace/config/portals.service /lib/systemd/system/

sudo -u postgres createdb portals
echo 'CREATE EXTENSION IF NOT EXISTS "pg_trgm";' | sudo -u postgres psql portals
echo 'CREATE EXTENSION IF NOT EXISTS "uuid-ossp";' | sudo -u postgres psql portals
echo "CREATE ROLE portals LOGIN PASSWORD 'portals' NOINHERIT NOCREATEDB;" | sudo -u postgres psql portals
echo 'CREATE SCHEMA portals AUTHORIZATION portals;' | sudo -u postgres psql portals
sudo -u portals psql < /workspace/schema/portals.sql

sudo systemctl daemon-reload
sudo systemctl enable portals
sudo systemctl restart portals
