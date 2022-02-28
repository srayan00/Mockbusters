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
     'rating' float(2,1),
     'cast_list' varchar(200)
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
     PRIMARY KEY ('movie_id', 'store_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;