del  playerWeb/migrations/00*.py
del  db.sqlite3

python manage.py makemigrations
python manage.py migrate