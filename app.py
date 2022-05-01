# instructions to run:
# in terminal:
# pip install virtualenv
# pip install flask
# pip install flask-sqlalchemy
# export FLASK_APP=app
# export FLASK_ENV=development
# flask run (or "python -m flask run" if that doesn't work)
# go to link/signup in the browser
import sqlite3
from sqlite3 import Error
from flask import Flask, redirect, url_for, request, render_template
import alchemy_init
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update

app = Flask(__name__)

database = 'Mockbusters.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Mockbusters.db'
db = SQLAlchemy(app)
if (db is None):
    raise ValueError("Could not initialize ORM: db is None")

alchemy_init.SQL_ALCHEMY_DB = db
from orm import Customer, Movie, Store, Catalog, Transactions, Active_Rentals

add_customer = """
    INSERT INTO Customer(customer_id, customer_name, customer_email)
    VALUES('%s','%s', '%s');
    """
check_store_id = """
   SELECT count(*) FROM Store where store_id = %d;
"""

check_username = """
SELECT count(*) FROM Customer WHERE Customer.customer_id = \'%s\';
"""

rent_movie = """
   INSERT INTO Active_Rentals (rental_id, movie_id, store_id, customer_id, date_rented, date_due, transaction_id)
   VALUES ((SELECT count(*) FROM Transactions) + 1, %d, %d, \'%s\', %s, %s, (SELECT count(*) FROM Transactions) + 1);
"""

get_most_recent_rental_id = """
SELECT count(*) FROM Transactions;
"""

find_movie_id_by_name = """
   SELECT movie_id FROM Movie WHERE movie_name LIKE \'%s\';
"""

get_curr_date = """
   SELECT DATE(\'now\');
"""

get_due_date = """
   SELECT DATE(\'now\', \'+7 days\');
"""

lookup_whole_catalog = """
SELECT c.movie_id, m.movie_name, m.genre, m.director_name, m.rating, m.cast_list, c.store_id, c.quantity_available, c.times_rented
FROM Movie m JOIN Catalog c ON m.movie_id = c.movie_id;

"""

check_catalog_combo = """
   SELECT count(*) FROM Catalog JOIN Movie ON Movie.movie_id = Catalog.movie_id
                  JOIN Store ON Store.store_id = Catalog.store_id
                  WHERE Movie.movie_name LIKE \'%s\'
                  AND (Store.store_id = %d
                  OR Store.zip_code LIKE \'%s\');"""

count_catalog_available = """SELECT Catalog.quantity_available FROM Catalog JOIN Movie ON Movie.movie_id = Catalog.movie_id
                  JOIN Store ON Store.store_id = Catalog.store_id
                  WHERE Movie.movie_name LIKE \'%s\'
                  AND (Store.store_id = %d
                  OR Store.zip_code LIKE \'%s\');"""

check_return_combo = """
   SELECT count(*) FROM Active_Rentals a
            WHERE a.rental_id = %d AND a.customer_id LIKE \'%s\';
            """

add_back_movie = """
      UPDATE Catalog SET quantity_available = quantity_available + 1
            WHERE Catalog.movie_id = (SELECT movie_id FROM Active_Rentals WHERE Active_Rentals.rental_id = %d)
            AND Catalog.store_ID = (SELECT store_id FROM Active_Rentals WHERE Active_Rentals.rental_id = %d); 
            """

remove_from_active_rentals = """
      DELETE FROM Active_Rentals WHERE Active_Rentals.rental_id = %d and Active_Rentals.customer_id = \'%s\';
      """


lookup_from_search = """
SELECT m.movie_id, m.movie_name, m.genre, m.director_name, m.rating, m.cast_list, Catalog.store_id, Catalog.quantity_available, Catalog.times_rented
FROM Movie as m
JOIN Catalog ON Catalog.movie_id = m.movie_id
WHERE m.movie_name LIKE \'%{}%\'
AND m.cast_list LIKE \'%{}%\'
AND m.director_name LIKE \'%{}%\'
AND m.genre LIKE \'%{}%\'
"""

@app.route('/successful_return/<user>/<movie_name>/<rental_id>')
def successful_return(user, movie_name, rental_id):
    # cnx = sqlite3.connect(database)
    # curs = cnx.cursor()
    ### ORM STARTS ###
    # curs.execute(add_back_movie % (int(rental_id), int(rental_id)))
    # cnx.commit()
    # curs.close()
    curr_rental = Active_Rentals.query.filter_by(rental_id = int(rental_id)).first()
    # curr_movie_id = curr_rental.movie_id
    # curr_store_id = curr_rental.store_id
    # catalog_d = Catalog.query.filter(movie_id == curr_movie_id, store_id == curr_store_id)
    # catalog_d.quantity_available = catalog_d.quantity_available + 1
    # db.session.commit()
    db.session.delete(curr_rental)
    db.session.commit()
    ### END ###
    # curs.execute(add_back_movie % (int(rental_id), int(rental_id)))
    # curs.execute(remove_from_active_rentals % (int(rental_id), str(user)))
    # cnx.commit()
    # curs.close()
    return 'Thank you for shopping with us, ' + user + '! You have successfully returned ' + movie_name + '!'


@app.route('/successful_rental/<count>/<user>/<store>/<movie>')
def successful_rental(count, user, store, movie):
    cnx = sqlite3.connect(database)
    curs = cnx.cursor()
    curs.execute(check_username % user)
    user_count = curs.fetchall()
    if user_count[0][0] == 1:
        if int(count) >= 1:
            # curs.execute(find_movie_id_by_name % (str(movie)))
            # movie_id = curs.fetchall()[0][0]
            ### ORM STARTS ###
            curr_movie = Movie.query.filter(Movie.movie_name.like(str(movie))).first()
            movie_id = curr_movie.movie_id
            ### END ###
            curs.execute(get_curr_date)
            curr_date = curs.fetchall()[0][0]
            curs.execute(get_due_date)
            due_date = curs.fetchall()[0][0]
            # curs.execute(get_most_recent_rental_id)
            ### ORM STARTS ###
            count_rent = Transactions.query.count()
            rental_id = count_rent + 1

            new_rental = Active_Rentals(rental_id = int(rental_id), movie_id = int(movie_id), store_id = int(store),
                                        customer_id = user, date_rented = curr_date, date_due = due_date, transaction_id =int(rental_id))
            db.session.add(new_rental)
            db.session.commit()
            ### END ###
            # curs.execute(rent_movie % (int(movie_id), int(store), user, curr_date, due_date))
            # curs.execute(get_most_recent_rental_id)
            # rental_id = curs.fetchall()[0][0]
            cnx.commit()
            curs.close()
            return 'successfully rented movie with rental id: ' + str(
                rental_id) + '. Save this rental id to make your return.'
        else:
            cnx.commit()
            curs.close()
            return movie + " is not available at store with id: " + store
    else:
        cnx.commit()
        curs.close()
        return 'oops! please go back and enter a valid username'


@app.route('/success/<count>/<user>/<name>/<email>')
def success(count, user, name, email):
    if count == '0':
        # cnx = sqlite3.connect(database)
        # curs = cnx.cursor()
        ### ORM STARTS ###
        new_customer = Customer(customer_id = user, customer_name = name, customer_email = email)
        db.session.add(new_customer)
        db.session.commit()
        ### END ###
        # curs.execute(add_customer % (user, name, email))
        # cnx.commit()
        # curs.close()
        return 'Successfully created username: ' + user
    else:
        return 'oops! username already exists, please go back and try again.'


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    # cnx = sqlite3.connect(database)
    # curs = cnx.cursor()
    if request.method == 'POST':
        ### ORM STARTS ###
        user = str(request.form['nm'])
        count = Customer.query.filter(Customer.customer_id == user).count()
        ### END ###
        # query = check_username % (str(user))
        # curs.execute(query)
        # count = curs.fetchall()
        # cnx.commit()
        # curs.close()
        return redirect(url_for('success', count=count, user=user, name=str(request.form['un']),
                                email=str(request.form['em'])))
    # curs.close()
    return render_template('signup.html')


@app.route('/rent', methods=['POST', 'GET'])
def rent():
    cnx = sqlite3.connect(database)
    curs = cnx.cursor()
    if request.method == 'POST':
        user = str(request.form['un'])
        movie_name = str(request.form['mn'])
        store_id = request.form['sid']
        curs.execute(check_catalog_combo % (str(movie_name), int(store_id), str(store_id)))
        check_catalog_count = curs.fetchall()[0][0]
        if check_catalog_count >= 1:
            curs.execute(count_catalog_available % (str(movie_name), int(store_id), str(store_id)))
            count = curs.fetchall()[0][0]
        else:
            count = 0
        cnx.commit()
        curs.close()
        return redirect(
            url_for('successful_rental', count=count, user=user, store=str(store_id), movie=str(movie_name)))
        # return render_template('successful_rental.html', count = count, user = user, movie = str(movie_name))
    curs.close()
    return render_template('rent.html')


@app.route('/return_movie', methods=['GET', 'POST'])
def return_movie():
    # cnx = sqlite3.connect(database)
    # curs = cnx.cursor()
    if request.method == 'POST':
        user = str(request.form['un'])
        movie_name = str(request.form['mn'])
        rental_id = request.form['rid']

        # checks if the username has a rental under that rental ID, returns 1 if it exists and 0 if it doesn't
        # curs.execute(check_return_combo % (int(rental_id), str(user)))
        # check_return_count = curs.fetchall()[0][0]
        ### ORM STARTS ###
        check_return_count = Active_Rentals.query.filter(Active_Rentals.rental_id == int(rental_id),
                                                         Active_Rentals.customer_id.like(str(user))).count()
        ### END ###
        print('check_return_count = ', check_return_count)

        if check_return_count >= 1:
            # cnx.commit()
            # curs.close()
            return redirect(url_for('successful_return', user=user, movie_name = str(movie_name),
                                    rental_id=str(rental_id)))
        else:
            # show unsuccessful page
            # cnx.commit()
            # curs.close()
            return "Incorrect username or rental id entered. Please go back and try again!"
    # curs.close()
    return render_template('return.html')


@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
   cnx = sqlite3.connect(database)
   curs = cnx.cursor()
   if request.method == 'POST':
      movie_name = str(request.form['mn'])
      actor_name = str(request.form['an'])
      director_name = str(request.form['dn'])
      genre = str(request.form['ge'])
      store_id = request.form['sid']
      yt = str(request.form.getlist('yt'))

      lookup_query = lookup_from_search.format(movie_name, actor_name, director_name, genre)
      if store_id.isnumeric():
         
         store_id_query = """ AND Catalog.store_id = {}"""
         lookup_query = lookup_query + store_id_query.format(int(store_id[0][0]))
      
      if ( str(yt)) != "" and 'on' in str(yt):
         lookup_query = lookup_query + """ ORDER BY Catalog.times_rented DESC""" 

      lookup_query = lookup_query + """;"""
      curs.execute(lookup_query)
      lookup_info = []
      for movie_id, movie_name, genre, director_name, rating, cast_list, store_id, quantity_available, times_rented in (curs.fetchall()):
         lookup_info.append((movie_id, movie_name, genre, director_name, rating, cast_list, store_id, quantity_available, times_rented))
      cnx.commit()
      curs.close()
      return (render_template('lookup.html', data = lookup_info))

   curs.execute(lookup_whole_catalog)

   lookup_info = []
   for movie_id, movie_name, genre, director_name, rating, cast_list, store_id, quantity_available, times_rented in (curs.fetchall()):
      lookup_info.append((movie_id, movie_name, genre, director_name, rating, cast_list, store_id, quantity_available, times_rented))
   cnx.commit()
   curs.close()
   return (render_template('lookup.html', data = lookup_info))


if __name__ == '__main__':
    app.run(debug=True)
