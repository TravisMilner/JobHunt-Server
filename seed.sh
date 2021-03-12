#!/bin/bash

rm -rf JobHuntapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations JobHuntapi
python3 manage.py migrate JobHuntapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata statuses
python3 manage.py loaddata jobs
python3 manage.py loaddata contacts
python3 manage.py loaddata companies


# Create a seed.sh file in your project directory
# Place the code below in the file.
# Run chmod +x seed.sh in the terminal.
# Then run ./seed.sh in the terminal to run the commands.