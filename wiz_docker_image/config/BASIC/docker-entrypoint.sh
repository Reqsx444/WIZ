#!/bin/bash
git clone -b ${BRANCH} https://${REPO}:${TOKEN}@gitlab.infracore.pl/wiz/${REPO}.git /var/WIZ/
pip install --no-cache-dir -r /var/WIZ/requirements.txt
python3 /var/WIZ/manage.py runserver 0.0.0.0:9099
