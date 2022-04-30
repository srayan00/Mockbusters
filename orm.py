from alchemy_init import SQL_ALCHEMY_DB as db


class Customer(db.Model):
    __tablename__ = "Customer"
    customer_id = db.Column(db.String(10), primary_key = True, nullable= False)
    customer_name = db.Column(db.String(20), nullable = False)
    customer_email = db.Column(db.String(20), nullable = False)

class Movie(db.Model):
    __tablename__ = "Movie"
    movie_id = db.Column(db.Integer, primary_key = True, nullable = False)
    movie_name = db.Column(db.String(20), nullable = False)
    genre = db.Column(db.String(10), nullable = False)
    director_name = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Float, nullable = False)
    cast_list = db.Column(db.String(20), nullable = False) # This should be a set


class Store(db.Model):
    __tablename__ = "Store"
    store_id = db.Column(db.Integer, primary_key = True, nullable = False)
    zip_code = db.Column(db.Integer, nullable = False)
    location_name = db.Column(db.String(20), nullable = False)



class Catalog(db.Model):
    __tablename__ = "Catalog"
    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.movie_id'), primary_key = True, nullable = False)
    store_id = db.Column(db.Integer, db.ForeignKey('Store.store_id'), primary_key = True, nullable = False)
    total_quantity = db.Column(db.Integer, nullable = False)
    quantity_available = db.Column(db.Integer, nullable = False)
    times_rented = db.Column(db.Integer, nullable = False)


class Transactions(db.Model) :
    __tablename__ = "Transactions"
    transaction_id = db.Column(db.Integer, primary_key=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey(Customer.customer_id), primary_key=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey(Store.store_id), primary_key=False, nullable=False)
    price = db.Column(db.Integer, primary_key = False, nullable = False)


class Active_Rentals(db.Model):
    __tablename__ = "Active_Rentals"
    rental_id = db.Column(db.Integer, primary_key=True, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.movie_id), primary_key = False, nullable = False)
    store_id = db.Column(db.Integer, db.ForeignKey(Store.store_id), primary_key = False, nullable = False)
    customer_id = db.Column(db.Integer, db.ForeignKey(Customer.customer_id), primary_key = False, nullable = False)
    date_rented = db.Column(db.Text, primary_key = False, nullable = False)
    date_due = db.Column(db.Text, primary_key=False, nullable=False)
    transaction_id = db.Column(db.Integer, db.ForeignKey(Transactions.transaction_id),
                               primary_key = False, nullable = False)


# def __init__(self, rental_id, movie_id, store_id, customer_id, date_rented, date_due, transaction_id):
#     self.rental_id = rental_id
#     self.movie_id = movie_id
#     self.store_id = store_id
#     self.customer_id = customer_id
#     self.date_rented = date_rented
#     self.date_due = date_due
#     self.transaction_id = transaction_id


db.create_all()
