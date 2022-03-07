
#instructions to run:
   # in terminal:
      # export FLASK_APP=app
      # export FLASK_ENV=development
      # flask run
   # go to filepath/login.html in the browser

# cnx = msql.connector.connect('mockbuster.db')

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/', methods=['GET', 'POST'])
def homepage():
   return render_template('homepage.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)


