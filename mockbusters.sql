DROP TABLE IF EXISTS 'Customer';
DROP TABLE IF EXISTS 'Movie';
DROP TABLE IF EXISTS 'Store';
DROP TABLE IF EXISTS 'Catalog';
DROP TABLE IF EXISTS 'Active_Rentals';
DROP TABLE IF EXISTS 'Transactions';

-- ----------------------------------------
 CREATE TABLE IF NOT EXISTS 'Customer'(
     --Attributes
     'customer_id' varchar(10) NOT NULL,
     'customer_name' varchar(10) NOT NULL, 
     'customer_email' varchar(20) NOT NULL,
     --Key
     PRIMARY KEY ('customer_id')
 );
-- ENGINE=InnoDB DEFAULT CHARSET=latin1;
 CREATE INDEX Customer ON Customer(customer_id);


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
 ) ;
 -- ENGINE=InnoDB DEFAULT CHARSET=latin1;
 CREATE INDEX Movie_Index ON Movie(movie_name);


 CREATE TABLE IF NOT EXISTS 'Store'(
     --Attributes
     'store_id' int(11) NOT NULL,
     'zip_code' varchar(5) NOT NULL, 
     'location_name' varchar(20) NOT NULL,
     --Key
     PRIMARY KEY ('store_id')
 ) ;
 -- ENGINE=InnoDB DEFAULT CHARSET=latin1;
  CREATE INDEX Store_Index ON Store(store_id);

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
 ) ;
 -- ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
 ) ;
 
 -- ENGINE=InnoDB DEFAULT CHARSET=latin1;

  CREATE TABLE IF NOT EXISTS 'Active_Rentals'(
     --Attributes
     'rental_id' int(11) NOT NULL,
     'movie_id' int(11) NOT NULL,
     'store_id' int(11) NOT NULL, 
     'customer_id' int(11) NOT NULL,
     'date_rented' text NOT NULL,
     'date_due' text NOT NULL,
     'transaction_id' int(11) NOT NULL,
     --Key
     PRIMARY KEY ('rental_id'),
     FOREIGN KEY ('movie_id') REFERENCES Movie('movie_id'),
     FOREIGN KEY ('store_id') REFERENCES Store('store_id'),
     FOREIGN KEY ('transaction_id') REFERENCES Transactions('transaction_id'),
     FOREIGN KEY ('customer_id') REFERENCES Customer('customer_id')
 ) ;
 -- ENGINE=InnoDB DEFAULT CHARSET=latin1;
 CREATE INDEX Rental_Index ON Active_Rentals(movie_id,store_id);


CREATE TRIGGER afterRentalInsert AFTER INSERT ON Active_Rentals FOR EACH ROW
    BEGIN
        INSERT INTO Transactions(transaction_id, customer_id, price, store_id)
        VALUES (NEW.transaction_id, NEW.customer_id, abs(JULIANDAY(NEW.date_due)- JULIANDAY(NEW.date_rented)) * 3, NEW.store_id);
    END;


CREATE TRIGGER updateCatalog AFTER INSERT ON Active_Rentals FOR EACH ROW
    BEGIN
        UPDATE Catalog SET quantity_available = quantity_available - 1 WHERE movie_id = NEW.movie_id AND store_id = NEW.store_id;
        UPDATE Catalog SET times_rented = times_rented + 1 WHERE movie_id = NEW.movie_id AND store_id = NEW.store_id;
    END;

CREATE TRIGGER returnCatalog BEFORE DELETE ON Active_Rentals FOR EACH ROW
    BEGIN
        UPDATE Catalog SET quantity_available = quantity_available + 1 
        WHERE movie_id = (SELECT movie_id FROM Active_Rentals WHERE Active_Rentals.rental_id = OLD.rental_id)
        AND Catalog.store_ID = (SELECT store_id FROM Active_Rentals WHERE Active_Rentals.rental_id = OLD.rental_id); 
    END;