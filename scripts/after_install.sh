#!/usr/bin/env bash

# kill any servers that may be running in the background 
sudo pkill -f runserver

# kill frontend servers if you are deploying any frontend
# sudo pkill -f tailwind
# sudo pkill -f node

cd /home/ec2-user/StudentSystem02/

# activate virtual environment
python3 -m venv venv
source venv/bin/activate

install requirements.txt
pip install -r /home/ec2-user/StudentSystem02/requirements.txt

# run server
screen -d -m python3 manage.py runserver 0:8080