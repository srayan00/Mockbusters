# instructions to run:
# in terminal:
# pip install virtualenv
# pip install flask
# export FLASK_APP=app
# export FLASK_ENV=development
# flask run (or "python -m flask run" if that doesn't work)
# go to link/signup in the browser
import sqlite3
from sqlite3 import Error


from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

database = 'Mockbusters.db'

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
   VALUES ((SELECT count(*) FROM Active_Rentals) + 1, %d, %d, \'%s\', %s, %s, (SELECT count(*) FROM Transactions) + 1);
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

@app.route('/sucessful_rental/<count>/<user>/<store>/<movie>')
def successful_rental(count, user, store, movie):
   cnx = sqlite3.connect(database)
   curs = cnx.cursor()
   curs.execute(check_username % (user))
   user_count = curs.fetchall()
   if user_count[0][0] == 1:
      if int(count) >= 1: 
         curs.execute(find_movie_id_by_name % (str(movie)))
         movie_id = curs.fetchall()[0][0]
         curs.execute(get_curr_date)
         curr_date = curs.fetchall()[0][0]
         curs.execute(get_due_date)
         due_date = curs.fetchall()[0][0]
         curs.execute(rent_movie % (int(movie_id), int(store), user, curr_date, due_date))
         cnx.commit()
         curs.close()
         return 'succesfully rented movie'
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
      cnx = sqlite3.connect(database)
      curs = cnx.cursor()
      curs.execute(add_customer % (user, name, email))
      cnx.commit()
      curs.close()
      return 'Successfully created username: ' + user
   else:
      return 'oops! username already exists, please go back and try again.'

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
   cnx = sqlite3.connect(database)
   curs = cnx.cursor()
   if request.method == 'POST':
      user = str(request.form['nm'])
      query  = check_username % (str(user))
      curs.execute(query)
      count = curs.fetchall()
      cnx.commit()
      curs.close()
      return redirect(url_for('success',count = count[0][0], user=user, name=str(request.form['un']), email=str(request.form['em'])))
   curs.close()
   return render_template('signup.html')

@app.route('/rent', methods=['POST', 'GET'])
def rent():
   cnx = sqlite3.connect(database)
   curs = cnx.cursor()
   if request.method == 'POST':
      user = str(request.form['un'])
      movie_name = str(request.form['mn'])
      store_id = request.form['sid']
      # temporarily expect exact movie name match because will add search result display later
      query  = """SELECT Catalog.quantity_available FROM Catalog JOIN Movie ON Movie.movie_id = Catalog.movie_id
               JOIN Store ON Store.store_id = Catalog.store_id
               WHERE Movie.movie_name LIKE \'""" + str(movie_name) + """\'
               AND (Store.store_id = """ + store_id + """
               OR Store.zip_code LIKE \'""" + str(store_id) + """\');"""
      curs.execute(query)
      count = curs.fetchall()
      cnx.commit()
      curs.close()
      return redirect(url_for('successful_rental',count = count[0][0], user=user, store=str(store_id), movie=str(movie_name)))
   curs.close()
   return render_template('rent.html')

@app.route('/return_movie', methods=['GET', 'POST'])
def return_movie():
    return render_template('return.html')

@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    return render_template('lookup.html')

# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(debug=True)
