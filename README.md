# Mockbusters

## Create Database and tables
To create Mockbusters.db and the tables, run this command in ther terminal:
```
sqlite3 Mockbusters.db < /Mockbusters/mockbusters.sql
```

## Populate the tables with sample data
Run load_csv.py file to fill the Store, Catalog, Movies, and Customer tables.
```
python3 load_csv.py
```
## Instructions to run app.py
In terminal, run
```
pip install virtualenv
pip install flask
pip install flask-sqlalchemy
export FLASK_APP=app
export FLASK_ENV=development
python -m flask run
```
Note that the above instructions may differ based on operating system type.

Go to http://127.0.0.1:5000/signup to signup

Go to http://127.0.0.1:5000/rent to rent a movie

