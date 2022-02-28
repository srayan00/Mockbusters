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
     'cast_list' SET(varchar(20), varchar(20), varchar(20))
     --Key
     PRIMARY KEY ('movie_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;


 CREATE TABLE IF NOT EXISTS 'Store'(
     --Attributes
     'store_id' int(11) NOT NULL,
     'zip_code' int(5) NOT NULL, 
     'location_name' varchar(20) NOT NULL,
     --Key
     PRIMARY KEY ('store_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

  CREATE TABLE IF NOT EXISTS 'Catelog'(
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


  CREATE TABLE IF NOT EXISTS 'Active_Rentals'(
     --Attributes
     'movie_id' int(11) NOT NULL,
     'store_id' int(11) NOT NULL, 
     'customer_id' int(11) NOT NULL,
     'date_rented' DATE NOT NULL,
     'date_due' DATE NOT NULL,
     'transaction_id' int(11) NOT NULL,
     --Key
     PRIMARY KEY ('transaction_id'),
     FOREIGN KEY ('movie_id') REFERENCES Movie('movie_id'),
     FOREIGN KEY ('store_id') REFERENCES Store('store_id'),
     FOREIGN KEY ('transaction_id') REFERENCES Transaction('transaction_id'),
     FOREIGN KEY ('customer_id') REFERENCES Customer('customer_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

 CREATE TABLE IF NOT EXISTS 'Transaction'(
     --Attributes
     'transaction_id' int(11) NOT NULL,
     'customer_id' int(11),
     'price' DECIMAL(8,2) NOT NULL, 
     'store_id' int(11) NOT NULL,
     --Key
     PRIMARY KEY ('transaction_id'),
     FOREIGN KEY ('customer_id') REFERENCES Customer('customer_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;