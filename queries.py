import os
import ui
import time
import yaml
import globl
import random
import datetime
import mysql.connector

from datetime import timedelta
from collections import defaultdict
from multiprocessing import Process
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import make_response

# Database queries
add_customer = """
    INSERT INTO Customer(customer_id, customer_name, customer_email)
    VALUES(%d,%s, %s);
    """

get_available_movies_by_zipcode = """
    SELECT Movie.movie_id, Movie.movie_name, Store.store_id
    FROM Catalog JOIN Movie ON Catalog.movie_id = Movie.movie_id
    JOIN Store ON Store.store_id = Catalog.store_id
    WHERE Catalog.quantity_available > 0
    AND Store.zip_code = %d;
    """

get_stores_having_movie = """
    SELECT Store.store_id, Store.location_name, Catalog.quantity_available
    FROM Catalog JOIN Movie on Catalog.movie_id = Movie.movie_id
    JOIN Store ON Store.store_id = Catalog.store_id
    WHERE Catalog.movie_name LIKE '*%s*'
    AND Catalog.quantity_available > 0;
    """

rent_movie_from_store = """
    INSERT INTO Active_Rentals (movie_id, store_id, customer_id, date_rented, date_due, transaction_id)
    VALUES (((SELECT count(*) FROM Transaction) + 1), %d, %d, )
    INSERT INTO Transaction (transaction_id, customer_id, price, store_id)
    VALUES(((SELECT count(*) FROM Transaction) + 1), %d, %.2f, %d);
"""

