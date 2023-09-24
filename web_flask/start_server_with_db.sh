#!/bin/bash

# Ensure the web_flask directory exists
mkdir -p web_flask

# Set environment variables
HBNB_MYSQL_USER=hbnb_dev
HBNB_MYSQL_PWD=hbnb_dev_pwd
HBNB_MYSQL_HOST=localhost
HBNB_MYSQL_DB=hbnb_dev_db
HBNB_TYPE_STORAGE=db

# Run the Flask application
python3 -m web_flask.$1 > /dev/null 2>&1 &

# Store the process ID (PID) in the .pid file
echo $! > web_flask/$1.pid

sleep 5

