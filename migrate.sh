rm -rf firmware/migrations/
rm -rf db.sqlite3
python3 manage.py makemigrations firmware
python3 manage.py migrate
python3 manage.py runserver