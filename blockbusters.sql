DROP TABLE IF EXISTS 'Customer';
DROP TABLE IF EXISTS 'Movie';
DROP TABLE IF EXISTS 'Store';
DROP TABLE IF EXISTS 'Catelog';
DROP TABLE IF EXISTS 'Active_Rentals';
DROP TABLE IF EXISTS 'Transactions';

-- ----------------------------------------
 CREATE TABLE IF NOT EXISTS 'Customer'(
     --Attributes
     'customer_id' int(11) NOT NULL,
     'customer_name' varchar(10) NOT NULL, 
     'customer_email' varchar(20) NOT NULL,
     --Key
     PRIMARY KEY ('customer_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;


 CREATE TABLE IF NOT EXISTS 'Movie'(
     --Attributes
     'movie_id' int(11) NOT NULL,
     'movie_name' varchar(20) NOT NULL, 
     'genre' varchar(10) NOT NULL,
     'director_name' varchar(20) NOT NULL,
     'rating' DECIMAL(2,1),
     'cast_list' text,
     --Key
     PRIMARY KEY ('movie_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;


 CREATE TABLE IF NOT EXISTS 'Store'(
     --Attributes
     'store_id' int(11) NOT NULL,
     'zip_code' varchar(5) NOT NULL, 
     'location_name' varchar(20) NOT NULL,
     --Key
     PRIMARY KEY ('store_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

  CREATE TABLE IF NOT EXISTS 'Catalog'(
     --Attributes
     'movie_id' int(11) NOT NULL,
     'store_id' int(11) NOT NULL, 
     'total_quantity' int(11) NOT NULL,
     'quantity_available' int(11) NOT NULL,
     'times_rented' int(11) NOT NULL,
     --Key
     PRIMARY KEY ('movie_id', 'store_id'),
     FOREIGN KEY ('movie_id') REFERENCES Movie('movie_id'),
     FOREIGN KEY ('store_id') REFERENCES Store('store_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

 CREATE TABLE IF NOT EXISTS 'Transactions'(
     --Attributes
     'transaction_id' int(11) NOT NULL,
     'customer_id' int(11),
     'price' DECIMAL(8,2) NOT NULL, 
     'store_id' int(11) NOT NULL,
     --Key
     PRIMARY KEY ('transaction_id'),
     FOREIGN KEY ('customer_id') REFERENCES Customer('customer_id'),
     FOREIGN KEY ('store_id') REFERENCES Store('store_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

  CREATE TABLE IF NOT EXISTS 'Active_Rentals'(
     --Attributes
     'rental_id' int(11) NOT NULL,
     'movie_id' int(11) NOT NULL,
     'store_id' int(11) NOT NULL, 
     'customer_id' int(11) NOT NULL,
     'date_rented' DATE NOT NULL,
     'date_due' DATE NOT NULL,
     'transaction_id' int(11) NOT NULL,
     --Key
     PRIMARY KEY ('rental_id'),
     FOREIGN KEY ('movie_id') REFERENCES Movie('movie_id'),
     FOREIGN KEY ('store_id') REFERENCES Store('store_id'),
     FOREIGN KEY ('transaction_id') REFERENCES Transactions('transaction_id'),
     FOREIGN KEY ('customer_id') REFERENCES Customer('customer_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

"""
    Genres: Children's Film, Comedy, Animation, Action, Adventure, Fantasy

    INSERT INTO Customer(customer_id, customer_name, customer_email)
    VALUES(1, 'Sarah', 'testemail0@purdue.edu');

    INSERT INTO Customer(customer_id, customer_name, customer_email)
    VALUES(2,'Nupur', 'testemail1@purdue.edu');

    INSERT INTO Customer(customer_id, customer_name, customer_email)
    VALUES(3, 'Nikita', 'testemail2@purdue.edu');

    INSERT INTO Customer(customer_id, customer_name, customer_email)
    VALUES(4, 'Sahana', 'testemail3@purdue.edu');

    INSERT INTO Movie(movie_id, movie_name, genre, director_name, rating, cast_list)
    VALUES(1, "Madagascar", "Children's Film, Comedy, Animation",
    'Tom McGrath, Eric Darnell', 4.9, 'Ben Stiller, Chris Rock, David Schwimmer, Jada Pinkett Smith');

    INSERT INTO Movie(movie_id, movie_name, genre, director_name, rating, cast_list)
    VALUES(3, "Madagascar: Escape 2 Africa", "Children's Film, Comedy, Animation",
    'Tom McGrath, Eric Darnell', 4.9, 'Ben Stiller, Chris Rock, Alec Baldwin, Jada Pinkett Smith');

    INSERT INTO Movie(movie_id, movie_name, genre, director_name, rating, cast_list)
    VALUES(2, "Madagascar 3: Europe's Most Wanted", "Children's Film, Comedy, Animation",
    'Tom McGrath, Eric Darnell', 4.9, 'Ben Stiller, Chris Rock, Alec Baldwin, Jada Pinkett Smith');

    INSERT INTO Store(store_id, zip_code, location_name)
    VALUES(1, "55598", "Los Angeles, CA");

    INSERT INTO Store(store_id, zip_code, location_name)
    VALUES(2, "55200", "Fremont, CA");

    INSERT INTO Store(store_id, zip_code, location_name)
    VALUES(3, "52034", "San Francisco, CA");

    INSERT INTO Catalog(movie_id, store_id, total_quantity, quantity_available, times_rented)
    VALUES(1, 2, 10, 3, 8);

    INSERT INTO Catalog(movie_id, store_id, total_quantity, quantity_available, times_rented)
    VALUES(3, 2, 10, 10, 2);

    INSERT INTO Catalog(movie_id, store_id, total_quantity, quantity_available, times_rented)
    VALUES(3, 1, 1, 1, 50);

    INSERT INTO Catalog(movie_id, store_id, total_quantity, quantity_available, times_rented)
    VALUES(3, 3, 4, 2, 10);

    INSERT INTO Catalog(movie_id, store_id, total_quantity, quantity_available, times_rented)
    VALUES(2, 3, 5, 4, 1);


