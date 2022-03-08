# instructions to run:
# in terminal:
# pip install virtualenv
# pip install flask
# export FLASK_APP=app
# export FLASK_ENV=development
# flask run (or "python -m flask run" if that doesn't work)
# go to filepath/login.html in the browser

# cnx = msql.connector.connect('mockbuster.db')

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    return render_template('signup.html')

@app.route('/rent', methods=['POST', 'GET'])
def ren():
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
