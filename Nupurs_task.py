from alchemy_init import SQL_ALCHEMY_DB as db


class Customer(db.Model):
    __tablename__ = "Customer"
    customer_id = db.Column(db.Integer, primary_key = True, nullable= False)
    customer_name = db.Column(db.String(20), nullable = False)
    customer_email = db.Column(db.String(20), nullable = False)

class Movie(db.Model):
    __tablename__ = "Movie"
    movie_id = db.Column(db.Integer, primary_key = True, nullable = False)
    movie_name = db.Column(db.String(20), nullable = False)
    genre = db.Column(db.String(10), nullable = False)
    director_name = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Float, nullable = False)
    cast_list = db.Column(db.String(20), nullable = False)


