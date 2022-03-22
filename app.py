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

add_customer = """
    INSERT INTO Customer(customer_id, customer_name, customer_email)
    VALUES('%s','%s', '%s');
    """

@app.route('/success/<count>/<user>/<name>/<email>')
def success(count, user, name, email):
   if count == '0':
      cnx = sqlite3.connect('Mockbusters.db')
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
   cnx = sqlite3.connect('Mockbusters.db')
   curs = cnx.cursor()
   if request.method == 'POST':
      user = str(request.form['nm'])
      query  = "SELECT count(*) FROM Customer WHERE Customer.customer_id = \'" + str(user) + "\';"
      curs.execute(query)
      count = curs.fetchall()
      cnx.commit()
      curs.close()
      return redirect(url_for('success',count = count[0][0], user=user, name=str(request.form['un']), email=str(request.form['em'])))
   curs.close()
   return render_template('signup.html')

@app.route('/rent', methods=['POST', 'GET'])
def rent():
   cnx = sqlite3.connect('Mockbusters.db')
   curs = cnx.cursor()
   if request.method == 'POST':
      movie_name = str(request.form['mn'])
      store_id = request.form['sid']
      query  = """SELECT count(*) FROM Catalog JOIN Movie ON Movie.movie_id = Catalog.movie_id
               JOIN Store ON Store.store_id = Catalog.store_id
               WHERE Movie.movie_name LIKE \'%""" + str(movie_name) + """%\'
               AND (Store.store_id = """ + store_id + """
               OR Store.zip_code LIKE \'""" + str(store_id) + """\');"""
      curs.execute(query)
      count = curs.fetchall()
      cnx.commit()
      curs.close()
      return render_template('rent.html')
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
