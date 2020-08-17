#!/bin/bash -
#===============================================================================
#
#          FILE: 0-setup_web_static.sh
#
#         USAGE: ./0-setup_web_static.sh
#
#   DESCRIPTION: Prepare your web servers
#
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: SAMUEL GOMEZ JIMENEZ (samgj18), samgomjim.18@gmail.com
#  ORGANIZATION: Holberton
#       CREATED: 17/08/2020 15:18:16
#      REVISION:  ---
#===============================================================================

set -o nounset                                  # Treat unset variables as an error

#!/usr/bin/env bash
# web server for deployment
sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" >/data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

new_str="location /hbnb_static {\nalias /data/web_static/current;\n}"
sudo sed -i "/# Only/ i $new_str" /etc/nginx/sites-enabled/default

sudo service nginx restart